import datetime
import functools
import uuid
from pathlib import Path

import fsspec
from pyogrio import read_info

from earthscale.auth import get_fsspec_storage_options
from earthscale.datasets.dataset import (
    Dataset,
    DatasetDefinition,
    DatasetMetadata,
    DatasetStatus,
    DatasetType,
    registry,
)
from earthscale.utils import create_valid_url

_DEFAULT_VECTOR_BAND = "default"


@functools.lru_cache
def _get_bounds(url: str) -> tuple[float, float, float, float]:
    extra_options = get_fsspec_storage_options(url)
    fs, _ = fsspec.url_to_fs(url, **extra_options)
    if not fs.exists(url):
        raise FileNotFoundError(f"File {url} does not exist.")
    with fs.open(url) as f:
        info = read_info(f, force_total_bounds=True)
    total_bounds: tuple[float, float, float, float] = info["total_bounds"]
    return total_bounds


class VectorDatasetDefinition(DatasetDefinition):
    url: str
    start_date_field: str | None
    end_date_field: str | None


class VectorDataset(Dataset[VectorDatasetDefinition]):
    """Dataset based on vector file

    Args:
        url:
            URL of the vector file
        name:
            Name of the dataset as shown in the platform
    """

    def __init__(
        self,
        url: str | Path,
        name: str | None = None,
        metadata: DatasetMetadata | None = None,
        start_date_field: str | None = None,
        end_date_field: str | None = None,
    ):
        # HACK: As we're re-writing the visualization logic, a vector dataset will just
        #       define a "default" visualization. Later-on users will be able to style
        #       the vector layer in the frontend.
        # TODO: do similar checks for value_map and colormap
        # if metadata is not None and len(metadata.visualizations) > 0:
        #     raise ValueError(
        #         "Vector datasets cannot have custom visualizations at the moment"
        #     )
        metadata = metadata or DatasetMetadata()

        explicit_name = name is not None
        name = name or str(uuid.uuid4())
        url = create_valid_url(str(url))
        self.url = url
        self.start_date_field = start_date_field
        self.end_date_field = end_date_field

        definition = VectorDatasetDefinition(
            url=str(url),
            start_date_field=start_date_field,
            end_date_field=end_date_field,
        )

        super().__init__(
            name,
            explicit_name,
            metadata,
            type_=DatasetType.VECTOR,
            status=DatasetStatus.NOT_STARTED,
            definition=definition,
        )

    def get_bounds(self) -> tuple[float, float, float, float]:
        return _get_bounds(str(self.url))

    def get_dates(self) -> list[datetime.datetime]:
        return []


registry.register_class("VectorDataset", VectorDataset)
