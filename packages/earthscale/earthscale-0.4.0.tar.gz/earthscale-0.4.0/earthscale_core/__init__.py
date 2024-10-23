from pystac import Item

from earthscale.datasets.raster import ImageDataset
from earthscale_core.repositories.stac import FlatgeobufSTACItemRepository
from earthscale_core.settings import Settings


def _get_stac_items(dataset_name: str) -> list[Item] | None:
    settings = Settings()
    root = settings.stac_item_repository_root
    if root == "":
        return None

    repo = FlatgeobufSTACItemRepository(root)
    return repo.get_items(dataset_name)


ImageDataset.register_get_items_callback(_get_stac_items)
