import datetime
import functools
import re
import time
import uuid
from collections import defaultdict
from collections.abc import Callable, Iterable, Sequence
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
from functools import cached_property
from pathlib import Path
from typing import Any, ClassVar, Generic, Literal, Union, cast

import contextily as ctx
import ee
import fsspec
import networkx as nx
import numpy as np
import odc.geo.xr
import odc.stac
import pandas as pd
import rasterio
import rioxarray  # noqa: F401
import xarray as xr
from affine import Affine
from loguru import logger
from networkx import is_directed_acyclic_graph
from odc.geo import Geometry, Resolution
from odc.geo.geobox import GeoBox
from odc.stac import output_geobox, parse_items
from pydantic import BaseModel
from pyproj import CRS
from pystac import Item
from rasterio.errors import RasterioIOError
from rasterio.io import DatasetReader
from rasterio.transform import from_bounds
from rio_stac import create_stac_item
from rio_stac.stac import RASTER_EXT_VERSION
from rioxarray.exceptions import OneDimensionalRaster
from shapely import MultiPolygon, Polygon, box
from stac_pydantic import Item as PydanticItem  # type: ignore

from earthscale.auth import (
    get_fsspec_storage_options,
    get_gdal_options_for_url,
    is_google_drive_url,
)
from earthscale.constants import (
    DEFAULT_CHUNKSIZES,
    MAX_NUM_EO_ASSET_BANDS,
    METERS_PER_DEGREE,
    XARRAY_CACHE_LEN,
)
from earthscale.datasets.dataset import (
    Dataset,
    DatasetDefinition,
    DatasetMetadata,
    DatasetStatus,
    DatasetType,
    DefinitionType,
    registry,
)
from earthscale.datasets.graph import (
    JoinNode,
    create_source_graph,
    get_dset_for_node,
    get_final_node_name,
    validate_graph,
)
from earthscale.exceptions import (
    EarthscaleError,
    convert_rasterio_to_earthscale,
)
from earthscale.types import BBOX, Chunksizes
from earthscale.utils import create_valid_url

Groupby = Literal["time"] | Literal["solar_day"] | Literal["id"] | str


class NoFilesForGlobError(EarthscaleError):
    """Raised when no files are found for a given glob pattern"""

    pass


class NoGeoboxError(EarthscaleError):
    """Raised when a dataset does not have a geobox set"""

    pass


class CannotConvertEarthEngineToXarrayError(EarthscaleError):
    """Raised when a user tries to call `.to_xarray()` for an earth engine dataset"""

    pass


class CacheEntry:
    def __init__(
        self,
        dset: xr.Dataset,
        bbox: BBOX | None,
        bands: Iterable[str] | None,
        chunksizes: Chunksizes,
    ):
        self.dset = dset
        self.bbox = bbox
        self.bands: tuple[str, ...] | None = tuple(bands) if bands is not None else None
        self.chunksizes = chunksizes


class DatasetCache:
    """Geo-aware cache for datasets, checking to see if we already
    have a dataset with the same bounding box and bands.

    Evicts the oldest entries first
    """

    def __init__(self, cache_len: int = 10):
        assert cache_len > 0
        self.cache_len = cache_len
        self.cache: dict[str, list[CacheEntry]] = defaultdict(list)
        self.most_recent_keys: list[str] = []

    def _total_length(self) -> int:
        return sum(len(v) for v in self.cache.values())

    def add(
        self,
        id: str,
        chunksizes: Chunksizes,
        bbox: BBOX | None,
        bands: Iterable[str] | None,
        dset: xr.Dataset,
    ) -> None:
        entry = CacheEntry(dset, bbox, bands, chunksizes)
        if id not in self.cache:
            self.cache[id] = []
        self.cache[id].append(entry)
        self.most_recent_keys.append(id)
        if self._total_length() > self.cache_len:
            oldest_key = self.most_recent_keys.pop(0)
            if len(self.cache[oldest_key]) > 0:
                self.cache[oldest_key].pop(0)
            else:
                # if the key no longer has any entries, remove it from the cache
                self.most_recent_keys = [
                    k for k in self.most_recent_keys if k != oldest_key
                ]

    def get(
        self,
        id: str,
        chunksizes: Chunksizes,
        bbox: BBOX | None,
        bands: Iterable[str] | None,
    ) -> xr.Dataset | None:
        entries = self.cache[id]
        self.most_recent_keys.append(id)
        for entry in entries:
            if entry.bands is None:
                is_bands_subset = True
            else:
                is_bands_subset = (bands is not None) and all(
                    band in entry.bands for band in bands
                )

            if entry.bbox is None:
                bbox_is_subset = True
            else:
                query_bbox = box(*bbox)
                cached_bbox = box(*entry.bbox)
                # We need a small buffer to account for floating point precision issues
                bbox_is_subset = cached_bbox.contains(
                    query_bbox.buffer(-1e-14)
                ) or cached_bbox.equals(query_bbox)
            if is_bands_subset and bbox_is_subset:
                return entry.dset
        return None


# Cache to avoid duplicate computations of `.to_xarray()` as that's expensive for large
# datasets
_XARRAY_CACHE = DatasetCache(cache_len=XARRAY_CACHE_LEN)
_DEFAULT_DATETIME = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)

# Arguments other than `geobox` that `odc.stac.load` uses for georeferencing
_GEOREFERENCING_ARGS = (
    "x",
    "y",
    "lon",
    "lat",
    "crs",
    "resolution",
    "align",
    "anchor",
    "like",
    "geopolygon",
    "bbox",
)


def _validate_dset(dset: xr.Dataset) -> None:
    assert isinstance(dset, xr.Dataset)
    dset_dimension_names = set(dset.sizes.keys())
    # On the dataset, the dimensions are always alphabetically sorted
    if "time" in dset_dimension_names:
        assert dset_dimension_names == {"time", "y", "x"}
    else:
        assert dset_dimension_names == {"y", "x"}
    for var in dset.data_vars:
        # On the data arrays, the order is important (y, x) so we can't do a set check
        darr_dimension_names = list(dset[var].dims)
        if "time" in darr_dimension_names:
            assert darr_dimension_names == ["time", "y", "x"]
        else:
            assert darr_dimension_names == ["y", "x"]
    assert "x" in dset.coords
    assert "y" in dset.coords
    assert dset.rio.crs is not None
    # assert dset.rio.crs == CRS.from_epsg(4326)


class RasterDataset(Generic[DefinitionType], Dataset[DefinitionType]):
    def __init__(
        self,
        name: str,
        explicit_name: bool,
        graph: nx.DiGraph,
        metadata: DatasetMetadata,
        definition: DefinitionType,
        geobox_callback: Callable[[], GeoBox],
        id: str | None = None,
    ):
        self._graph = graph
        self._geobox_callback = geobox_callback
        validate_graph(self._graph)

        super().__init__(
            name,
            explicit_name,
            metadata,
            type_=DatasetType.RASTER,
            # Raster datasets are ready by default
            status=DatasetStatus.READY,
            definition=definition,
            id=id,
        )

    @property
    def geobox(self) -> GeoBox:
        return self._geobox_callback()

    def get_bounds(self) -> tuple[float, float, float, float]:
        # Always returns the bounds in EPSG:4326
        return cast(
            tuple[float, float, float, float],
            tuple(self._geobox_callback().boundingbox.to_crs(4326)),
        )

    def get_dates(self) -> list[datetime.datetime]:
        raise NotImplementedError

    def join(
        self,
        # Union is required here instead of `|` as that won't work with a string
        others: Union[Sequence["RasterDataset[Any]"], "RasterDataset[Any]"],
        match: "RasterDataset[Any]",
        name: str | None = None,
        metadata: DatasetMetadata | None = None,
    ) -> "RasterDataset[Any]":
        if isinstance(others, RasterDataset):
            others = [others]
        explicit_name = name is not None
        name = name or str(uuid.uuid4())
        new_graph = self._graph.copy()
        join_node_name = f"join_{name}"
        node = JoinNode(
            match_name=match.name,
            output_name=name,
            output_metadata=metadata,
        )
        new_graph.add_node(
            join_node_name,
            node=node,
        )
        # Connect this dataset to the join node
        new_graph.add_edge(
            get_final_node_name(self._graph),
            join_node_name,
        )
        # Connect all other datasets to the join node
        geobox = self.geobox
        for other in others:
            new_graph = nx.union(new_graph, other._graph)
            new_graph.add_edge(
                get_final_node_name(other._graph),
                join_node_name,
            )
            geobox = geobox & other.geobox
        return RasterDataset(
            name,
            explicit_name,
            new_graph,
            metadata or DatasetMetadata(),
            definition=DatasetDefinition(),
            geobox_callback=lambda: geobox,
        )

    def to_xarray(
        self,
        # The bounding box is assumed to be in EPSG:4326. Might lead to speedups for
        # certain dataset types (e.g. STAC and ImageDataset)
        bbox: BBOX | None = None,
        # Subset of bands to return. Might lead to speedup for certain dataset types
        # (e.g. STAC and ImageDataset)
        bands: Iterable[str] | None = None,
        chunksizes: Chunksizes | None = None,
    ) -> xr.Dataset:
        if chunksizes is None:
            chunksizes = DEFAULT_CHUNKSIZES

        cached_dset: xr.Dataset | None = _XARRAY_CACHE.get(
            self.id,
            chunksizes,
            bbox,
            bands,
        )
        if cached_dset is not None:
            logger.debug(
                f"Found xr.Dataset for dataset with id '{self.id}', bounds '{bbox}', "
                f"bands '{bands}' and chunksizes '{chunksizes}' in the cache, using "
                f"that"
            )
            return cached_dset
        start_time = time.time()
        assert is_directed_acyclic_graph(self._graph)
        final_node_name = get_final_node_name(self._graph)
        dset = get_dset_for_node(self._graph, final_node_name, bbox, bands, chunksizes)

        # While the datasets already have information about the `bbox` and `bands`
        # arguments, cropping them again here just to be certain as it should not lead
        # to a performance hit
        if bbox is not None:
            try:
                # We try clipping with clip_box first, as that should be more performant
                dset = dset.rio.clip_box(*bbox, crs=CRS.from_epsg(4326))
            except OneDimensionalRaster:
                # We try with more exact clipping if the above fails because the area
                # is smaller than a pixel
                dset = dset.rio.clip(
                    [box(*bbox)],
                    crs=CRS.from_epsg(4326),
                    # All touched is important here to get at leas one pixel
                    all_touched=True,
                )
        if bands is not None:
            dset = dset[bands]

        _validate_dset(dset)
        _XARRAY_CACHE.add(
            self.id,
            chunksizes,
            bbox,
            bands,
            dset,
        )
        logger.debug(
            f".to_xarray() for dataset with id '{self.id}', bounds '{bbox}', bands "
            f"'{bands}' and chunsizes '{chunksizes}' took {time.time() - start_time} "
            f"seconds"
        )
        return dset

    def get_polygon(self, polygon: Polygon | MultiPolygon) -> xr.Dataset:
        dset = self.to_xarray()
        clipped_to_bounds = dset.rio.clip_box(*polygon.bounds)
        clipped = clipped_to_bounds.rio.clip([polygon])
        return cast(xr.Dataset, clipped)


def _get_dates_from_dataset(dataset: RasterDataset[Any]) -> list[datetime.datetime]:
    # TODO(remove_to_xarray): We can probably do this without a `to_xarray()` call
    #                         based on the dataset metadata
    dset = dataset.to_xarray()
    if "time" in dset.sizes:
        dates: list[datetime.datetime] = dset.time.dt.date.values.tolist()
    else:
        dates = []
    return dates


class ZarrDatasetDefinition(DatasetDefinition):
    store: str
    rename: dict[str, str] | None
    kw_args: dict[str, Any] | None


class ZarrDataset(RasterDataset[ZarrDatasetDefinition]):
    """Dataset based on a Zarr store.

    Args:
        store:
            The Zarr store to load the dataset from.
        name:
            The name of the dataset. Defaults to a random UUID. If explicitly given, the
            dataset will be visible in the Earthscale platform.

    """

    def __init__(
        self,
        store: str | Path,
        name: str | None = None,
        metadata: DatasetMetadata | None = None,
        rename: dict[str, str] | None = None,
        **kwargs: Any | None,
    ):
        explicit_name = name is not None
        name = name or str(uuid.uuid4())

        self._store = store
        self._rename = rename
        self._kwargs = kwargs

        definition = ZarrDatasetDefinition(
            store=str(store),
            rename=rename,
            kw_args=kwargs,
        )

        # There's no use for bbox or bands here as the performance is the same whether
        # the whole dataset metadata is loaded or not
        def load(
            bbox: BBOX | None,
            bands: Iterable[str] | None,
            chunksizes: Chunksizes | None,
        ) -> xr.Dataset:
            logger.debug("Calling load function for ZarrDataset")
            return _load_zarr_dataset(
                store=store,
                rename=rename or {},
                **kwargs,
            )

        graph = create_source_graph(
            f"load_zarr_dataset_{name}",
            name,
            metadata,
            load,
        )

        super().__init__(
            name=name,
            explicit_name=explicit_name,
            graph=graph,
            metadata=metadata or DatasetMetadata(),
            # We want the geobox of the full dataset as well as all bands here, so not
            # passing a bounding box here
            geobox_callback=lambda: load(
                bbox=None,
                bands=None,
                chunksizes=None,
            ).odc.geobox,
            definition=definition,
        )

    def get_dates(self) -> list[datetime.datetime]:
        return _get_dates_from_dataset(self)


# Using a lower `maxsize` as the images are potentially quite large
@functools.lru_cache(maxsize=10)
def _convert_stac_items_to_geobox(
    items: tuple[Item, ...],
    bands: tuple[str, ...] | None,
    **kwargs: Any,
) -> GeoBox:
    logger.debug("Converting STAC items to geobox")
    geobox = output_geobox(
        items=list(parse_items(items)),
        bands=bands,
        crs=kwargs.get("crs"),
        resolution=kwargs.get("resolution"),
        anchor=kwargs.get("anchor"),
        align=kwargs.get("align"),
        geobox=kwargs.get("geobox"),
        like=kwargs.get("like"),
        geopolygon=kwargs.get("geopolygon"),
        bbox=kwargs.get("bbox"),
        lon=kwargs.get("lon"),
        lat=kwargs.get("lat"),
        x=kwargs.get("x"),
        y=kwargs.get("y"),
    )
    if geobox is None:
        raise ValueError("Could not determine geobox for dataset")
    return geobox


class STACDatasetDefinition(DatasetDefinition):
    items: list[PydanticItem]
    bands: list[str] | None
    groupby: Groupby | None
    kw_args: dict[str, Any] | None


class STACDataset(RasterDataset[STACDatasetDefinition]):
    """Spatio-Temporal Asset Catalog (STAC) based dataset

    Args:
        items:
            Items to build the dataset from. We allow passing in serialized stac items
            (dicts) as well.

        bands:
            List of bands to load. Defaults to all bands

        groupby:
            Controls what items get placed in to the same pixel plane.

            The following have special meaning:

               * "time" items with exactly the same timestamp are grouped together
               * "solar_day" items captured on the same day adjusted for solar time
               * "id" every item is loaded separately

            Any other string is assumed to be a key in Item's properties dictionary.
            Please note that contrary to `odc.stac.load` we do not support callables as
            we need to be able to serialize the dataset.

        name:
            Name of the dataset. Defaults to a random UUID. If explicitly given,
            The dataset will visible in the Earthscale platform

        metadata:
            Dataset Metadata. Defaults to None.

        kwargs:
            Additional keyword arguments to pass to
            [`odc.stac.load`](https://odc-stac.readthedocs.io/en/latest/_api/odc.stac.load.html)
            Only serializable arguments can be passed to STAC.
    """

    def __init__(
        self,
        items: list[Item | dict[str, Any]],
        bands: list[str] | None = None,
        groupby: Groupby | None = None,
        name: str | None = None,
        metadata: DatasetMetadata | None = None,
        **kwargs: Any | None,
    ):
        parsed_items = [
            Item.from_dict(item) if not isinstance(item, Item) else item
            for item in items
        ]

        metadata = metadata or DatasetMetadata()
        explicit_name = name is not None
        name = name or str(uuid.uuid4())
        geobox = _convert_stac_items_to_geobox(
            tuple(parsed_items),
            tuple(bands) if bands else None,
            **kwargs,
        )

        definition = STACDatasetDefinition(
            items=[PydanticItem(**item.to_dict()) for item in parsed_items],
            bands=bands,
            groupby=groupby,
            kw_args=kwargs,
        )

        def _load_stac_dataset_wrapper(
            bbox: BBOX | None,
            bands_selection: Iterable[str] | None,
            chunksizes: Chunksizes | None,
        ) -> xr.Dataset:
            # If a particular `to_xarray` call requests all bands, but
            # the dataset was created with a subset of bands, we need
            # to respect that and not load all bands from the STAC
            # items.
            if bands and not bands_selection:
                bands_selection = bands
            return _load_stac_dataset(
                items=parsed_items,
                bands=bands_selection,
                groupby=groupby,
                full_geobox=geobox,
                bbox=bbox,
                chunksizes=chunksizes,
                **kwargs,
            )

        super().__init__(
            name=name or str(uuid.uuid4()),
            explicit_name=explicit_name,
            graph=create_source_graph(
                f"load_file_dataset_{name}", name, metadata, _load_stac_dataset_wrapper
            ),
            metadata=metadata,
            geobox_callback=lambda: geobox,
            definition=definition,
        )

    def get_dates(self) -> list[datetime.datetime]:
        return _get_dates_from_dataset(self)


class BandInfoRow(BaseModel):
    index: int
    name: str
    datetime: str | None = None
    min: float | None = None
    max: float | None = None

    # TODO: add validation for datetime


def _band_info_df_to_list(df: pd.DataFrame) -> list[BandInfoRow]:
    # convert any datetimes to isoformat
    if "datetime" in df.columns:
        df["datetime"] = df["datetime"].apply(lambda x: x.isoformat())
    return [BandInfoRow(index=idx, **row.to_dict()) for idx, row in df.iterrows()]


def _band_info_list_to_df(band_info: list[BandInfoRow]) -> pd.DataFrame:
    df = pd.DataFrame(band_info)
    if "datetime" in df.columns:
        df["datetime"] = pd.to_datetime(df["datetime"])

    # Drop datetime, min or max column if all values are NaN
    df = df.dropna(axis=1, how="all")
    if "index" in df.columns:
        df = df.set_index("index")
    return df


class ImageDatasetDefinition(DatasetDefinition):
    glob_url: str
    bands: list[str] | None
    band_info: list[BandInfoRow] | None
    groupby: Groupby | None
    datetime_: datetime.datetime | tuple[datetime.datetime, datetime.datetime] | None
    filename_date_pattern: str | None
    kw_args: dict[str, Any]


class ImageDataset(RasterDataset[ImageDatasetDefinition]):
    """Dataset based on single images.

     Images must be in a format that can be read by `rasterio`. Under the hood, an
     `ImageDataset` creates a list of STAC items and then uses `odc.stac.load` to load
     the dataset.

     An important concept here is how the time dimension of the `Dataset` is set and
     which images account for which time.

     To group images by time (and thus create a time dimension), you can use the
     `groupby` argument. For more information on the options, please refer to the
     documentation of `odc.stac.load`
     ([here](https://odc-stac.readthedocs.io/en/latest/_api/odc.stac.load.html)). Note
     that as we need to serialize the class, we do not allow callables to be passed in.

     As images generally don't have time information, we provide several ways to set the
     time interval for an image. Only one of the following options can be set:

     1. `band_info`: A pandas DataFrame with band information. This is used to parse
        TIFF band indices into band name and datetime information.
     2. `datetime_`: Either a single `datetime.datetime` or a tuple of two
        `datetime.datetime` objects. If a single `datetime.datetime` is provided, all
        images will have the same timestamp. If a tuple is provided, the first element
        will be the start time and the second element will be the end time. This
        interval will be used for all images. This will result in all images having the
        same time interval.

    Args:
       glob_url:
           URL pattern to find images with. E.g. `gs://bucket/path/to/images/*.tif`.
       bands:
           List of bands to load. Defaults to all bands.
       band_info:
           DataFrame with band information. Defaults to None. This is used to provide
           metadata about bands in the images. It maps the band index to the band name
           and optionally time, min and max values. The index of the dataframe should be
           the band index (0-indexed). The following columns can be present:
             - name (str; required): The name of the band
             - datetime (datetime.datetime; optional): The datetime of the band
             - min (float; optional): The minimum value of the band
             - max (float; optional): The maximum value of the band
           We also allow this to be passed in as a dictionary of
           {column -> {index -> value}}.
       filename_date_pattern:
            A string pattern representing how dates are formatted in the filenames.
            This pattern uses strftime-style format codes to extract date information.

            Common format codes:
            %Y - Year with century as a decimal number (e.g., 2023)
            %m - Month as a zero-padded decimal number (01-12)
            %d - Day of the month as a zero-padded decimal number (01-31)

            Example:
            - For files named like "brasil_coverage_2011.tif":
              filename_date_pattern="%Y"

            If None (default), no date information will be extracted from filenames.
       groupby:
            Controls what items get placed in to the same pixel plane.

            The following have special meaning:

               * "time" items with exactly the same timestamp are grouped together
               * "solar_day" items captured on the same day adjusted for solar time
               * "id" every item is loaded separately

            Any other string is assumed to be a key in Item's properties dictionary.
            Please note that contrary to `odc.stac.load` we do not support callables as
            we need to be able to serialize the dataset.
       datetime_:
           Either a single `datetime.datetime` or a tuple of two `datetime.datetime`
           objects. If a single `datetime.datetime` is provided, all images will have
           the same time. If a tuple is provided, the first element will be the start
           time and the second element will be the end time. This interval will be
           valid for all images.
       name:
           Name of the dataset. Defaults to a random UUID. If explicitly given, the
           dataset will visible in the Earthscale platform
       metadata:
           Dataset Metadata. Defaults to None.
       kwargs:
           Additional keyword arguments to pass to `odc.stac.load`
           (more information in
           [their docs](https://odc-stac.readthedocs.io/en/latest/_api/odc.stac.load.html))

    """

    _GET_ITEMS_CALLBACK: ClassVar[Callable[[str], list[Item] | None] | None] = None

    @classmethod
    def register_get_items_callback(
        cls, callback: Callable[[str], list[Item] | None]
    ) -> None:
        cls._GET_ITEMS_CALLBACK = callback

    def __init__(
        self,
        glob_url: str,
        bands: list[str] | None = None,
        band_info: pd.DataFrame | list[BandInfoRow] | None = None,
        filename_date_pattern: str | None = None,
        groupby: Groupby | None = None,
        datetime_: datetime.datetime
        | tuple[datetime.datetime, datetime.datetime]
        | None = None,
        name: str | None = None,
        metadata: DatasetMetadata | None = None,
        **kwargs: Any | None,
    ):
        metadata = metadata or DatasetMetadata()
        explicit_name = name is not None
        name = name or str(uuid.uuid4())
        glob_url = create_valid_url(glob_url)

        # Only one of band_info or datetime_ can be provided.
        num_date_mechanisms = sum(1 for x in [band_info, datetime_] if x is not None)
        at_most_one_date_mechanism = num_date_mechanisms <= 1
        if not at_most_one_date_mechanism:
            raise ValueError(
                "Exactly one of band_info or datetime_ must be provided to set the "
                "time interval of the provided images."
            )

        if band_info is not None:
            if isinstance(band_info, list):
                band_info = _band_info_list_to_df(band_info)
            _validate_band_info_dataframe(band_info)
            has_min = "min" in band_info.columns
            has_max = "max" in band_info.columns
            has_only_one_of_min_max = has_min != has_max
            if has_only_one_of_min_max:
                raise ValueError(
                    "If specifying min and max values for a band, both must be provided"
                )
            if has_min and has_max:
                _update_min_max_metadata(metadata, band_info)

        definition = ImageDatasetDefinition(
            glob_url=glob_url,
            bands=bands,
            band_info=_band_info_df_to_list(band_info)
            if band_info is not None
            else None,
            groupby=groupby,
            datetime_=datetime_,
            filename_date_pattern=filename_date_pattern,
            kw_args=kwargs,
        )

        super().__init__(
            name=name,
            explicit_name=explicit_name,
            graph=create_source_graph(
                f"load_file_dataset_{name}",
                name,
                metadata,
                lambda bbox, bands_selection, chunksizes: _load_stac_dataset(
                    items=self._items,
                    bands=bands_selection,
                    groupby=groupby,
                    full_geobox=self.geobox,
                    bbox=bbox,
                    chunksizes=chunksizes,
                    band_info=band_info,
                    **kwargs,
                ),
            ),
            metadata=metadata,
            definition=definition,
            geobox_callback=lambda: _convert_stac_items_to_geobox(
                tuple(self._items),
                tuple(self.definition.bands) if self.definition.bands else None,
                **self.definition.kw_args,
            ),
        )

    @cached_property
    def _items(self) -> list[Item]:
        if ImageDataset._GET_ITEMS_CALLBACK is not None:
            items = ImageDataset._GET_ITEMS_CALLBACK(self.id)
            if items:
                return items
        return self.get_items()

    def get_items(self) -> list[Item]:
        if ImageDataset._GET_ITEMS_CALLBACK is not None:
            items = ImageDataset._GET_ITEMS_CALLBACK(self.id)
            if items:
                return items

        logger.debug("Computing items for ImageDataset")
        if self.definition.band_info is not None:
            band_info = _band_info_list_to_df(self.definition.band_info)
        else:
            band_info = None

        # There is no (tested) implementation of fsspec for Google Drive. There is
        # https://github.com/fsspec/gdrivefs but it isn't tested and has no support for
        # shared drives (which we definitely need).
        # As Google Drive does not have globs anyway, we can just return the original
        # URL
        if is_google_drive_url(self.definition.glob_url):
            image_urls = [self.definition.glob_url]
        else:
            fs, _ = fsspec.url_to_fs(
                self.definition.glob_url,
                **get_fsspec_storage_options(self.definition.glob_url),
            )
            image_urls = [
                fs.unstrip_protocol(path) for path in fs.glob(self.definition.glob_url)
            ]
        if len(image_urls) == 0:
            raise NoFilesForGlobError(
                f"No files found for glob: {self.definition.glob_url}"
            )

        items = _create_stac_items_from_urls(
            urls=image_urls,
            datetime_=self.definition.datetime_,
            band_info=band_info,
            filename_date_pattern=self.definition.filename_date_pattern,
        )
        return items

    def get_dates(self) -> list[datetime.datetime]:
        return _get_dates_from_dataset(self)


def _update_min_max_metadata(
    metadata: DatasetMetadata, band_info: pd.DataFrame
) -> None:
    """Updates min/max values if both are present in the band info"""
    bands = list(band_info["name"].unique())
    metadata.bands = bands

    rows_with_min_max = band_info[band_info["min"].notna() & band_info["max"].notna()]
    bands_with_min_max = list(rows_with_min_max["name"].unique())

    # Add validation if they only provide min or max, but not both for one band.
    rows_with_only_min = band_info[band_info["min"].notna() & band_info["max"].isna()]
    rows_with_only_max = band_info[band_info["min"].isna() & band_info["max"].notna()]
    if len(rows_with_only_min) > 0 or len(rows_with_only_max) > 0:
        raise ValueError(
            "If specifying min and max values for a band, both must always be provided."
        )

    min_max_values: dict[str, tuple[float | None, float | None]] = {}
    for band in bands_with_min_max:
        orig_band_min = band_info[band_info["name"] == band]["min"].min()
        orig_band_max = band_info[band_info["name"] == band]["max"].max()
        try:
            band_min = float(orig_band_min)
            band_max = float(orig_band_max)
        except Exception as e:
            raise ValueError(
                f"Could not convert min or max values ({orig_band_min}, {orig_band_max}"
                f") for band {band} to float: {e}"
            ) from e
        min_max_values[band] = (band_min, band_max)
    metadata.min_maxes_per_band = min_max_values


def _load_zarr_dataset(
    store: str | Path,
    rename: dict[str, str],
    **kwargs: Any | None,
) -> xr.Dataset:
    if kwargs is None:
        kwargs = {}

    if "decode_coords" not in kwargs:
        # Required to load CRS correctly
        kwargs["decode_coords"] = "all"

    # .get_mapper inspired by: https://github.com/fsspec/filesystem_spec/issues/386
    dset = xr.open_zarr(
        fsspec.get_mapper(
            store,
            **get_fsspec_storage_options(str(store)),
        ),
        **kwargs,
    )
    dset = dset.rename(rename)
    return cast(xr.Dataset, dset)


def _parse_datetime_from_string(
    date_string: str, date_format: str
) -> datetime.datetime:
    # Find date format as substring in date_string
    date_format_index = date_string.find(date_format)
    if date_format_index == -1:
        raise ValueError(f"Date format {date_format} not found in {date_string}")
    date_substring = date_string[
        date_format_index : date_format_index + len(date_format)
    ]
    return datetime.datetime.strptime(date_substring, date_format)


def _load_stac_dataset(  # noqa: C901
    items: list[Item],
    bands: Iterable[str] | None,
    groupby: Groupby | None,
    # Geobox of the full dataset, enabling a subselection of bbox in the same pixel grid
    full_geobox: GeoBox | None = None,
    # BBOX is assumed to be in EPSG:4326
    bbox: BBOX | None = None,
    chunksizes: Chunksizes | None = None,
    band_info: pd.DataFrame | None = None,
    **kwargs: Any | None,
) -> xr.Dataset:
    if chunksizes is None:
        chunksizes = DEFAULT_CHUNKSIZES

    bbox_geobox = None
    if bbox is not None:
        original_items = items
        if full_geobox is None:
            raise ValueError(
                "Cannot provide a bounding box without a full geobox of the dataset"
            )

        # Not 100% sure whether this filtering is strictly necessary, but the time to
        # filter the elements is negligible
        bbox_geometry = box(*bbox)
        original_number_of_items = len(items)
        items = [item for item in items if box(*item.bbox).intersects(bbox_geometry)]

        if len(items) == 0:
            logger.info(
                "After filtering by date and bounding box, no STAC items remain. This"
                "can happen if the underlying items don't fully cover the whole "
                "spatio-temporal extent. We're resetting to using all items to make "
                "sure downstream code works as expected."
            )
            items = original_items
        else:
            logger.debug(
                f"Bounding box filtering reduced the number of items from "
                f"{original_number_of_items} to {len(items)}"
            )

        bbox_geometry = Geometry(box(*bbox), "EPSG:4326")
        bbox_geobox = full_geobox.enclosing(bbox_geometry)
        # When geobox is provided kwargs must not include any other georeferencing
        # arguments
        for arg in _GEOREFERENCING_ARGS:
            if arg in kwargs:
                del kwargs[arg]

    if kwargs is None:
        kwargs = {}

    selected_bands: list[str] | None = None

    # We've had some trouble with datetime serialization, so we're making sure the
    # datetime column is always of the correct type
    if band_info is not None and "datetime" in band_info.columns:
        band_info["datetime"] = pd.to_datetime(band_info["datetime"])

    # The bands will be named `asset.<band_index>` (with 1-indexed band index)
    if band_info is not None and bands is not None:
        rows_for_name = band_info[band_info["name"].isin(bands)]
        selected_bands = [f"asset.{index + 1}" for index in rows_for_name.index]
    elif bands is not None:
        selected_bands = list(bands)

    # We only support TIFF files for now. Some STAC catalogs of interest have
    # non-raster assets such as J2 files so we exclude those.
    filtered_items = []
    for item in items:
        filtered_assets = {
            key: asset
            for key, asset in item.assets.items()
            if asset.media_type and "image/tiff" in asset.media_type.lower()
        }
        if filtered_assets:
            filtered_item = item.clone()
            filtered_item.assets = filtered_assets
            filtered_items.append(filtered_item)

    items = filtered_items
    logger.debug(f"Filtered to {len(items)} items with 'image/tiff' assets")

    # Clearing the `eo:bands.name` property if there are too many bands.
    # We're clearing that to have deterministic band names (`asset.<i>`) in the output
    # dset.
    # Generally, this is not great as we're loosing information present in the STAC
    # items, so we'll need to find a better solution there in the future.
    # Having the eo:bands.name property present does incur a significant performance hit
    # if the dataset has many bands though
    use_asset_based_naming = True
    for item in items:
        for asset in item.assets.values():
            if "eo:bands" in asset.extra_fields:
                num_bands = len(asset.extra_fields["eo:bands"])
                use_asset_based_naming = num_bands > MAX_NUM_EO_ASSET_BANDS
                if use_asset_based_naming:
                    for band in asset.extra_fields["eo:bands"]:
                        if "name" in band:
                            del band["name"]

    if use_asset_based_naming and band_info is not None:
        logger.warning(
            "Using asset-based naming for dataset because it either lacks eo:bands "
            f"metadata or has more than {MAX_NUM_EO_ASSET_BANDS} bands. "
            "Assets will be named `asset.<i>` (1-indexed) instead of `band_name`. "
            "To specify band names, use the `band_info` argument."
        )

    start_time = time.time()

    # Using the first item here to determine the GDAL options, assumes the whole
    # collection is homogeneous
    first_url = next(iter(items[0].assets.values())).href
    gdal_options = get_gdal_options_for_url(first_url)
    odc.stac.configure_rio(**gdal_options)  # type: ignore

    logger.debug(f"odc.stac.load called with {len(items)} items")
    try:
        dset = odc.stac.load(
            items=items,
            bands=selected_bands,
            groupby=groupby,
            # This will overwrite any other georeferencing settings such as CRS, x/y,
            # etc. Given that we're only doing this for a bounding box of the "original"
            # dataset this should be ok.
            geobox=bbox_geobox,
            chunks=chunksizes,  # type: ignore
            **kwargs,  # type: ignore
        )
    except RasterioIOError as e:
        raise convert_rasterio_to_earthscale(e) from e
    logger.debug(f"odc.stac.load took {time.time() - start_time} seconds")

    # In the case there's only one band, the band name is sometimes "asset" instead of
    # "asset.1". Fixing that here to make sure downstream code works as expected
    if len(dset.data_vars) == 1 and "asset" in dset.data_vars:
        dset = dset.rename_vars({"asset": "asset.1"})

    # At the moment, the downstream code is assuming no band names are present (e.g.
    # through the `eo:bands.name` STAC extension, just making sure that's the case.
    # Without the band names, we're expecting the data vars to be called `asset.<i>`
    # where `i` is the 1-indexed band index.
    if use_asset_based_naming:
        expected_band_name = re.compile(r"asset\.\d")
        for data_var in dset.data_vars:
            data_var = cast(str, data_var)
            if not expected_band_name.match(data_var):
                raise ValueError(
                    f"Found a data variable {data_var} that does not match the"
                    f"expected pattern 'asset.<i>'"
                )

    # If CRS is WGS84, odc will rename to lat/lng but we require x/y
    rename = {}
    if "longitude" in dset.sizes or "longitude" in dset.coords:
        rename["longitude"] = "x"
    if "latitude" in dset.sizes or "latitude" in dset.coords:
        rename["latitude"] = "y"
    dset = dset.rename(rename)

    if band_info is not None:
        dset = reshape_dset_to_band_info(dset, bands, band_info)

    if groupby is not None and "time" in dset.sizes:
        # Making sure time is always a date and not a datetime as we only support
        # dates for now
        times = dset["time"].compute()
        dates = times.dt.date.values
        dset["time"] = [
            datetime.datetime(date.year, date.month, date.day) for date in dates
        ]

    # Transpose back to rioxarray conventions
    if "time" in dset.sizes:
        dset = dset.transpose("time", "y", "x")
    else:
        dset = dset.transpose("y", "x")

    # If all dates are equal to _DEFAULT_TIMESTAMP, we assume no time information
    # has been passed in
    if "time" in dset.sizes:
        dset_times = dset["time"].values
        if len(dset_times) == 1 and dset_times[0] == np.datetime64(_DEFAULT_DATETIME):
            dset = dset.isel(time=0)

    return dset


# Copied from rio-stac
# https://github.com/developmentseed/rio-stac/blob/52a13eec0c8ad19dee904b2bc0cd529b73b95899/rio_stac/stac.py#
# but removed stats creation for performance reasons as it takes too long for rasters
# with a lot of bands and we don't use it yet
def _get_raster_info(src_dst: DatasetReader) -> list[dict[str, Any]]:
    """Get raster metadata.

    see: https://github.com/stac-extensions/raster#raster-band-object

    """
    meta: list[dict[str, Any]] = []

    area_or_point = src_dst.tags().get("AREA_OR_POINT", "").lower()

    # Missing `bits_per_sample` and `spatial_resolution`
    for band in src_dst.indexes:
        value = {
            "data_type": src_dst.dtypes[band - 1],
            "scale": src_dst.scales[band - 1],
            "offset": src_dst.offsets[band - 1],
        }
        if area_or_point:
            value["sampling"] = area_or_point

        # If the Nodata is not set we don't forward it.
        if src_dst.nodata is not None:
            if np.isnan(src_dst.nodata):
                value["nodata"] = "nan"
            elif np.isposinf(src_dst.nodata):
                value["nodata"] = "inf"
            elif np.isneginf(src_dst.nodata):
                value["nodata"] = "-inf"
            else:
                value["nodata"] = src_dst.nodata

        if src_dst.units[band - 1] is not None:
            value["unit"] = src_dst.units[band - 1]

        meta.append(value)

    return meta


def get_band_key(name: str, datetime_: datetime.datetime) -> str:
    return f"{name}-{datetime_.isoformat()}"


def reshape_dset_to_band_info(
    dset: xr.Dataset,
    bands: Iterable[str] | None,
    band_info: pd.DataFrame,
) -> xr.Dataset:
    """
    ODC STAC output dataset originally has one data variable per datetime+band.
    This function reshapes it to have one data variable per band, with
    datetimes as coordinates.
    """
    dataarrays_per_band = defaultdict(list)

    relevant_band_info = band_info
    if bands is not None:
        relevant_band_info = band_info[band_info["name"].isin(bands)]

    if "datetime" in relevant_band_info.columns:
        for row_index, row in relevant_band_info.iterrows():
            if not isinstance(row_index, int):
                raise ValueError(
                    "The index of the band info dataframe must be an integer"
                )
            # Band names will be `asset.<i>` (1-indexed)
            current_band_name = f"asset.{row_index + 1}"
            new_band_name = row["name"]
            dataarray = (
                dset[current_band_name]
                .squeeze()
                .expand_dims({"time": [row["datetime"]]})
            )
            dataarrays_per_band[new_band_name].append(dataarray)
        # Concatenate all DataArrays along the time dimension
        concatenated_dataarrays = {
            band_name: xr.concat(dataarrays, dim="time")
            for band_name, dataarrays in dataarrays_per_band.items()
        }
        # convert back to Dataset
        new_dset = xr.Dataset(concatenated_dataarrays)
    else:
        rename_dict = {
            f"asset.{cast(int, i) + 1}": row["name"]
            for i, row in relevant_band_info.iterrows()
        }
        new_dset = dset.rename_vars(rename_dict)

    return new_dset


def _create_stac_item_from_one_url(
    ds: DatasetReader,
    datetime_: datetime.datetime | tuple[datetime.datetime, datetime.datetime] | None,
    properties: dict[str, Any] | None,
) -> Item:
    raster_bands = _get_raster_info(ds)

    item: Item = create_stac_item(
        ds,
        input_datetime=datetime_,
        with_proj=True,
        # We are not adding the `eo` extension as that adds a significant overhead to
        # `odc.stac.load`
        with_eo=False,
        properties=properties,
    )
    item.stac_extensions.append(
        f"https://stac-extensions.github.io/raster/{RASTER_EXT_VERSION}/schema.json",
    )
    assert len(item.assets) == 1
    first_asset = next(iter(item.assets.values()))
    first_asset.extra_fields["raster:bands"] = raster_bands
    return item


def _get_datetime_and_properties_for_url(
    url: str,
    datetime_: datetime.datetime | tuple[datetime.datetime, datetime.datetime] | None,
    filename_date_pattern: str | None,
    band_info: pd.DataFrame | None,
) -> tuple[datetime.datetime | None, dict[str, Any]]:
    """
    Get the datetime and start/end datetime Item properties for a given URL.
    """
    final_datetime = None
    datetime_props = {}

    if isinstance(datetime_, datetime.datetime):
        final_datetime = datetime_
    elif isinstance(datetime_, tuple):
        datetime_props["start_datetime"] = datetime_[0].isoformat()
        datetime_props["end_datetime"] = datetime_[1].isoformat()
        final_datetime = None
    elif filename_date_pattern is not None:
        try:
            final_datetime = _parse_datetime_from_string(url, filename_date_pattern)
        except ValueError as e:
            logger.error(f"Failed to parse datetime from asset {url}: {e}")
            raise e
    elif band_info is not None and "datetime" in band_info.columns:
        min_datetime = band_info["datetime"].min()
        max_datetime = band_info["datetime"].max()
        datetime_props["start_datetime"] = min_datetime.isoformat()
        datetime_props["end_datetime"] = max_datetime.isoformat()
        final_datetime = None
    else:
        final_datetime = _DEFAULT_DATETIME

    return final_datetime, datetime_props


def _create_stac_items_from_urls(
    urls: list[str],
    datetime_: datetime.datetime | tuple[datetime.datetime, datetime.datetime] | None,
    filename_date_pattern: str | None,
    band_info: pd.DataFrame | None,
) -> list[Item]:
    # In the case no time information is provided, we default to the Unix epoch.
    # The time information will be set by the bands on the outside.
    if datetime_ is None:
        datetime_ = _DEFAULT_DATETIME

    properties = {}
    if isinstance(datetime_, tuple):
        properties["start_datetime"] = datetime_[0].isoformat()
        properties["end_datetime"] = datetime_[1].isoformat()
        datetime_ = None

    def process_url(
        url: str,
    ) -> Item:
        url_properties = deepcopy(properties)
        url_datetime, datetime_props = _get_datetime_and_properties_for_url(
            url, datetime_, filename_date_pattern, band_info
        )
        url_properties.update(datetime_props)

        gdal_options = get_gdal_options_for_url(url)
        try:
            with rasterio.Env(**gdal_options), rasterio.open(url, "r") as ds:
                return _create_stac_item_from_one_url(ds, url_datetime, properties)
        except RasterioIOError as e:
            if "GS_SECRET_ACCESS_KEY" in e.args[0]:
                logger.error(
                    f"Error opening {url}. Do you have the correct credentials"
                    " to access this dataset?"
                )
            raise e

    logger.info(f"Processing {len(urls)} URLs")

    with ThreadPoolExecutor(max_workers=128) as executor:
        items = list(executor.map(lambda url: process_url(url), urls))
    return items


def _validate_band_info_dataframe(df: pd.DataFrame) -> None:
    """
    Validate the band info dataframe
    """
    required_columns = {"name"}
    optional_columns = {"min", "max", "datetime"}
    if not required_columns.issubset(df.columns.tolist()):
        raise ValueError(
            f"Band info dataframe must have the following columns: {required_columns}"
        )
    has_extra_columns = set(df.columns.tolist()) - required_columns - optional_columns
    if has_extra_columns:
        raise ValueError(
            f"Band info dataframe has the following extra columns: {has_extra_columns}"
        )

    if "datetime" in df.columns:
        # Check that across each band name, the set of datetimes is the same
        unique_datetimes_per_band = df.groupby("name")["datetime"].unique()
        unique_datetimes = unique_datetimes_per_band.iloc[0]
        for band, datetimes in unique_datetimes_per_band.items():
            if not np.array_equal(unique_datetimes, datetimes):
                raise ValueError(
                    f"Band {band} has different datetimes than the first band. "
                    f"All bands must have the same set of datetimes."
                )


def _convert_resolution_to_degrees(resolution: float, input_crs: CRS) -> float:
    unit_name = input_crs.axis_info[0].unit_name
    unit_conversion_factor = input_crs.axis_info[0].unit_conversion_factor
    if unit_name not in ["degree", "degrees"]:
        resolution_in_meters = resolution * unit_conversion_factor
        resolution = resolution_in_meters / METERS_PER_DEGREE
    return resolution


def _get_crs_from_ee_image(image: ee.Image) -> CRS:
    projection = image.projection().getInfo()
    if "crs" in projection:
        crs = CRS.from_string(projection["crs"])
    elif "wkt" in projection:
        crs = CRS.from_string(projection["wkt"])
    else:
        raise ValueError("Could not determine CRS from EE image")
    return crs


def _load_geobox_from_ee_image_collection(
    image_collection: ee.ImageCollection,
) -> GeoBox:
    number_of_images = image_collection.size().getInfo()

    # We return all of our geoboxes as WGS84
    crs = CRS.from_string("EPSG:4326")

    # In case we've got exactly one image, we can perfectly reconstruct the geobox
    if number_of_images == 1:
        image = image_collection.first()
        resolution_crs = _get_crs_from_ee_image(image)
        if crs is None:
            raise ValueError("The provided EE image does not have a valid CRS.")
        transform = Affine(*image.projection().getInfo()["transform"])
        bbox = Polygon(image.geometry().bounds().getInfo()["coordinates"][0]).bounds

    # In case we've got <10_000 images in the collection, we can still compute the
    # bounds and the merged CRS will be WGS84. 10_000 here was determined empirically.
    # If the number is too high, `.geometry()` will fail due to a memory error on EE.
    # We'll get the resolution from the first image, assuming all other images have
    # the same
    elif number_of_images < 10_000:
        first_image = ee.Image(image_collection.first())
        resolution_crs = _get_crs_from_ee_image(first_image)
        transform = Affine(*first_image.projection().getInfo()["transform"])
        bbox = Polygon(
            image_collection.geometry().bounds().getInfo()["coordinates"][0]
        ).bounds

    # If both of the above fail, we fall back to a "whole world geobox" using the
    # resolution of the first image
    else:
        first_image = ee.Image(image_collection.first())
        resolution_crs = _get_crs_from_ee_image(first_image)
        transform = Affine(*first_image.projection().getInfo()["transform"])
        bbox = (-180, -90, 180, 90)

    resolution = (
        _convert_resolution_to_degrees(transform.a, resolution_crs),
        _convert_resolution_to_degrees(transform.e, resolution_crs),
    )
    geobox = GeoBox.from_bbox(
        bbox=bbox,
        crs=crs,
        resolution=Resolution(*resolution),
    )
    return geobox


# Separate function to help with debugging
def _fail_when_loading_ee() -> xr.Dataset:
    raise CannotConvertEarthEngineToXarrayError(
        "Due to limitations in the metadata that Earth Engine provides on "
        "ImageCollections, we cannot load this dataset as an xarray Dataset."
    )


class EarthEngineDatasetDefinition(DatasetDefinition):
    # JSON serialized version of the ee.ImageCollection object
    image_collection: dict[str, Any]
    quality_band: str | None
    viz_params: dict[str, Any] | None


class EarthEngineDataset(RasterDataset[EarthEngineDatasetDefinition]):
    """
    Load data from Earth Engine.

    Args:
        image_collection:
            Either an ee.ImageCollection object or JSON dict of the image collection
        quality_band:
            The band used to determine the pixel ordering in the mosaic creation. Please
            refer to the [Earth-engine docs](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-qualitymosaic)
            for an example.
        viz_params:
            Visualization parameters for the mosaic. Please refer to the docs on
            [Image Visualization](https://developers.google.com/earth-engine/guides/image_visualization)
            on what's possible here.

            An example here would be:
            ```python
            viz_params = {
                "bands": ["B4", "B3", "B2"],
                "min": [0, 0, 0],
                "max": [0.3, 0.3, 0.3]
            }
            ```

        name:
            The name of the dataset. Defaults to a random UUID. If explicitly given, the
            dataset will be visible in the Earthscale platform.
    """

    def __init__(
        self,
        image_collection: ee.ImageCollection | dict[str, Any],
        quality_band: str | None = None,
        viz_params: dict[str, Any] | None = None,
        name: str | None = None,
        metadata: DatasetMetadata | None = None,
    ):
        if isinstance(image_collection, dict):
            image_collection = ee.ImageCollection(
                ee.deserializer.decode(image_collection)
            )
        explicit_name = name is not None
        name = name or str(uuid.uuid4())

        definition = EarthEngineDatasetDefinition(
            image_collection=ee.serializer.encode(image_collection),
            quality_band=quality_band,
            viz_params=viz_params,
        )

        if quality_band is None:
            image = image_collection.mosaic()
        else:
            image = image_collection.qualityMosaic(quality_band)

        if metadata is None:
            metadata = DatasetMetadata()

        if viz_params is None:
            viz_params = {}
        else:
            # Earthengine expects viz params to be a comma-separated string
            viz_params = {
                k: ",".join(map(str, v)) if isinstance(v, list) else str(v)
                for k, v in viz_params.items()
            }

        if metadata.tileserver_url is None:
            metadata.tileserver_url = ee.data.getMapId({"image": image, **viz_params})[
                "tile_fetcher"
            ].url_format

        super().__init__(
            name=name,
            explicit_name=explicit_name,
            graph=create_source_graph(
                f"load_earthengine_dataset_{name}",
                name,
                metadata,
                lambda bbox, bands_selection, chunksizes: _fail_when_loading_ee(),
            ),
            metadata=metadata or DatasetMetadata(),
            definition=definition,
            geobox_callback=lambda: _load_geobox_from_ee_image_collection(
                image_collection
            ),
        )

    def get_dates(self) -> list[datetime.datetime]:
        return []


class TileServerDatasetDefinition(DatasetDefinition):
    url: str


class TileServerDataset(RasterDataset[TileServerDatasetDefinition]):
    """
    Load data from a tile server.

    Args:
        url (str): The URL of the tile server with x, y, z placeholders, e.g.
            `https://server.com/tiles/{z}/{x}/{y}.png`.
        name (str, optional): The name of the dataset. Defaults to a random UUID.
            If explicitly given, the dataset will be visible in the Earthscale platform.
    """

    def __init__(
        self,
        url: str,
        name: str | None = None,
        metadata: DatasetMetadata | None = None,
        definition: TileServerDatasetDefinition | None = None,
    ):
        explicit_name = name is not None
        name = name or str(uuid.uuid4())

        definition = definition or TileServerDatasetDefinition(url=url)

        if metadata is None:
            metadata = DatasetMetadata()
        metadata.tileserver_url = url

        super().__init__(
            name=name,
            explicit_name=explicit_name,
            graph=create_source_graph(
                f"load_tileserver_dataset_{name}",
                name,
                metadata,
                self._load,
            ),
            metadata=metadata,
            geobox_callback=self._geobox_callback,
            definition=definition,
        )

    def _load(
        self,
        bbox: BBOX | None,
        bands: Iterable[str] | None,
        chunksizes: Chunksizes | None,
    ) -> xr.Dataset:
        # Define the bounds, either from bbox or default to global extent
        if bbox is not None:
            # bbox is in (left, bottom, right, top) in WGS84
            left, bottom, right, top = bbox
        else:
            # Default to global extent in WGS84
            left, bottom, right, top = (-180, -85.0511, 180, 85.0511)

        # Fetch the image
        img, extent = ctx.bounds2img(
            left,
            bottom,
            right,
            top,
            ll=True,
            zoom="auto",
            source=self.definition.url,
        )

        # img is an array of shape (height, width, bands)
        # extent is (left, bottom, right, top) in Web Mercator (EPSG:3857)

        # Create coordinates
        x = np.linspace(extent[0], extent[1], img.shape[1])
        y = np.linspace(extent[3], extent[2], img.shape[0])

        # Create dataset with x and y coordinates
        dset = xr.Dataset(
            coords={
                "x": ("x", x),
                "y": ("y", y),
            }
        )

        # Set band names and create data variables
        num_bands = img.shape[2]
        if num_bands == 3:
            band_names = ["red", "green", "blue"]
        elif num_bands == 4:
            band_names = ["red", "green", "blue", "alpha"]
        else:
            band_names = [f"band_{i+1}" for i in range(num_bands)]

        for i, band_name in enumerate(band_names):
            dset[band_name] = xr.DataArray(
                img[:, :, i],
                dims=("y", "x"),
                coords={"x": x, "y": y},
            )

        # Set CRS
        dset.rio.write_crs("EPSG:3857", inplace=True)

        if bands is not None:
            dset = dset[bands]

        return dset

    def _geobox_callback(self) -> GeoBox:
        # Default to global extent in Web Mercator (EPSG:3857)
        left, bottom, right, top = (
            -20037508.34,
            -20037508.34,
            20037508.34,
            20037508.34,
        )
        width, height = 256, 256  # Default tile size
        crs = "EPSG:3857"

        transform = from_bounds(
            west=left,
            south=bottom,
            east=right,
            north=top,
            width=width,
            height=height,
        )
        geobox = GeoBox((height, width), transform, crs)
        return geobox

    def get_dates(self) -> list[datetime.datetime]:
        return []


registry.register_class("ZarrDataset", ZarrDataset)
registry.register_class("STACDataset", STACDataset)
registry.register_class("ImageDataset", ImageDataset)
registry.register_class("EarthEngineDataset", EarthEngineDataset)
registry.register_class("TileServerDataset", TileServerDataset)
