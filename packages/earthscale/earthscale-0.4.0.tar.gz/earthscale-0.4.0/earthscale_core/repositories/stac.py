import abc
import concurrent.futures
import json
from typing import Any

import fsspec
import geopandas as gpd
from pystac import Item
from shapely.geometry import box


class AbstractSTACItemRepository(abc.ABC):
    @abc.abstractmethod
    def get_items(self, dataset_id: str) -> list[Item] | None:
        raise NotImplementedError

    @abc.abstractmethod
    def add_items(self, dataset_name: str, items: list[Item]) -> None:
        raise NotImplementedError


class FlatgeobufSTACItemRepository(AbstractSTACItemRepository):
    def __init__(self, root_url: str):
        self._root_url = root_url.rstrip("/")

    def get_items(self, dataset_name: str) -> list[Item] | None:
        storage_url = f"{self._root_url}/{dataset_name}.fgb"
        filesystem, _ = fsspec.url_to_fs(storage_url)
        if not filesystem.exists(storage_url):
            return None

        with filesystem.open(storage_url, "rb") as f:
            gdf = gpd.read_file(f)

        # Parse the items from the GeoDataFrame
        items = [
            Item.from_dict(json.loads(item["json"]))
            for item in gdf.to_dict(orient="records")
        ]
        return items

    def add_items(self, dataset_name: str, items: list[Item]) -> None:
        storage_url = f"{self._root_url}/{dataset_name}.fgb"
        filesystem, _ = fsspec.url_to_fs(storage_url)

        def process_item(item: Item) -> dict[str, Any]:
            return {"geometry": box(*item.bbox), "json": item.to_dict()}

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(process_item, items))

        crs = "EPSG:4326"

        if len(results) > 0:
            gdf = gpd.GeoDataFrame(results, crs=crs)
        else:
            gdf = gpd.GeoDataFrame(geometry=[], crs=crs)

        # Write the GeoDataFrame to a FlatGeobuf file
        with filesystem.open(storage_url, "wb") as f:
            gdf.to_file(f, driver="FlatGeobuf")
