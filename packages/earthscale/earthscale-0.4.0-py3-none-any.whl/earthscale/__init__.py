# We're adding a noqa here as dataset needs to be imported before the DatasetRepository
import os
from typing import Any

from loguru import logger

# from earthscale.aoi import AOI
from earthscale.auth import get_supabase_client
from earthscale.datasets.dataset import Dataset, DatasetDomain

# from earthscale.repositories.aoi import AOIRepository
from earthscale.repositories.dataset import DatasetRepository
from earthscale.utils import running_in_notebook


def _register_dataset(dataset: Dataset[Any]) -> None:
    supabase_client = get_supabase_client()
    dataset_repo = DatasetRepository(supabase_client, domain=DatasetDomain.WORKSPACE)
    logger.info(f"Registering dataset {dataset.name}")
    dataset_repo.add(dataset)


def _load_dataset(
    name: str,
    domain: DatasetDomain | None,
    version: str | None,
) -> Dataset[Any]:
    supabase_client = get_supabase_client()
    # HACK: temporarily disable creation callbacks to prevent double-registration
    original_callbacks = Dataset._DATASET_CREATION_CALLBACKS
    Dataset._DATASET_CREATION_CALLBACKS = []
    try:
        dataset_repo = DatasetRepository(
            supabase_client, domain=domain, version=version
        )
        dataset = dataset_repo.get_by_name(name)
    finally:
        Dataset._DATASET_CREATION_CALLBACKS = original_callbacks
    return dataset


# def _load_aoi(name: str) -> AOI:
#     supabase_client = get_supabase_client()
#     aoi_repo = AOIRepository(supabase_client)
#     return aoi_repo.get_by_name(name)


# Enable registration of datasets outside of the notebook context
_ALWAYS_REGISTER = os.getenv("EARTHSCALE_ALWAYS_REGISTER", None) is not None

# In the case of running the SDK in a notebook, we want to register datasets
# automatically
if running_in_notebook() or _ALWAYS_REGISTER:
    Dataset.register_dataset_creation_callback(_register_dataset)

Dataset.register_dataset_load_callback(_load_dataset)
# AOI.register_aoi_load_callback(_load_aoi)

__all__ = [
    "Dataset",
    "DatasetDomain",
]
