from typing import Any

from pydantic import BaseModel

from earthscale import DatasetDomain
from earthscale.datasets.dataset import Dataset, DatasetMetadata, DatasetType, registry


class DatasetRegistrationRequest(BaseModel):
    @classmethod
    def from_dataset(
        cls,
        dataset: Dataset[Any],
        domain: DatasetDomain,
    ) -> "DatasetRegistrationRequest":
        return cls(
            id=dataset.id,
            name=dataset.name,
            metadata=dataset.metadata,
            type=dataset.type,
            domain=domain,
            class_name=registry.get_registry_name(type(dataset)),
            dataset_definition=dataset.definition.model_dump(mode="json"),
        )

    id: str
    name: str
    metadata: DatasetMetadata
    type: DatasetType
    domain: DatasetDomain
    class_name: str
    dataset_definition: dict[str, Any]
