import abc
import datetime
import enum
import uuid
from collections.abc import Callable
from copy import deepcopy
from dataclasses import field
from enum import Enum
from typing import Any, ClassVar, Generic, TypeVar

from pydantic import BaseModel


class DatasetDefinition(BaseModel):
    """Holds all additional values required to reconstruct the dataset"""


class DatasetMetadata(BaseModel):
    # TODO: can't do dict[str, int] | dict[str, list[int]]?
    # throws mypy error when instantiated
    value_map: dict[str, int] | dict[str, list[int]] = field(default_factory=dict)
    bands: list[str] = field(default_factory=list)
    min_zoom: int | None = None
    min_maxes_per_band: dict[str, tuple[float | None, float | None]] | None = None
    # For some datasets/sources it is beneficial to use an external tileserver instead
    # of ours (e.g. earth-engine)
    tileserver_url: str | None = None


class DatasetDomain(str, Enum):
    """Defines which type of catalog a dataset belongs to."""

    WORKSPACE = "WORKSPACE"
    CATALOG = "CATALOG"


class DatasetType(enum.Enum):
    RASTER = "raster"
    VECTOR = "vector"


class DatasetStatus(enum.Enum):
    NOT_STARTED = "not_started"
    PROCESSING = "processing"
    PROCESSING_FAILED = "processing_failed"
    READY = "ready"


DefinitionType = TypeVar("DefinitionType", bound=DatasetDefinition)


class Dataset(abc.ABC, Generic[DefinitionType]):
    # List of functions to call when a dataset is created. This is useful in the case
    # of the SDK which can auto-register a callback when running in a notebook
    _DATASET_CREATION_CALLBACKS: ClassVar[list[Callable[["Dataset[Any]"], None]]] = []
    _DATASET_LOAD_CALLBACK: ClassVar[
        Callable[[str, DatasetDomain | None, str | None], "Dataset[Any]"] | None
    ] = None

    @classmethod
    def register_dataset_creation_callback(
        cls, callback: Callable[["Dataset[Any]"], None]
    ) -> None:
        cls._DATASET_CREATION_CALLBACKS.append(callback)

    @classmethod
    def register_dataset_load_callback(
        cls, callback: Callable[[str, DatasetDomain | None, str | None], "Dataset[Any]"]
    ) -> None:
        cls._DATASET_LOAD_CALLBACK = callback

    def __init__(
        self,
        name: str,
        explicit_name: bool,
        metadata: DatasetMetadata,
        type_: DatasetType,
        status: DatasetStatus,
        definition: DefinitionType,
        id: str | None = None,
    ):
        self.name = name
        self.metadata = metadata
        self.type = type_
        self.status = status
        self.id = id or str(uuid.uuid4())
        self._explicit_name = explicit_name
        self.definition = definition

        if explicit_name:
            # Used for e.g. registering in the Notebook case
            for callback in self._DATASET_CREATION_CALLBACKS:
                callback(self)

    @classmethod
    def load(
        cls,
        name: str,
        domain: DatasetDomain | None = None,
        version: str | None = None,
    ) -> "Dataset[DefinitionType]":
        if cls._DATASET_LOAD_CALLBACK is None:
            raise ValueError("No dataset load callback registered")
        return cls._DATASET_LOAD_CALLBACK(name, domain, version)

    @classmethod
    def from_serialized_definition(
        cls,
        name: str,
        metadata: DatasetMetadata,
        definition: dict[str, Any],
    ) -> "Dataset[DefinitionType]":
        definition = deepcopy(definition)
        kw_args = definition.pop("kw_args", {})

        return cls(
            name=name,
            metadata=metadata,
            **definition,
            **kw_args,
        )

    def serialize_definition(self) -> dict[str, Any]:
        return self.definition.model_dump(mode="json")

    @property
    def is_internally_visualizable(self) -> bool:
        """Whether we can internally visuzalize the dataset

        Some dataset types, such as Earth Engine use an external tile server. This
        removes the need for us to collect visualization metadata upon registration.

        """
        return self.metadata.tileserver_url is None

    @abc.abstractmethod
    def get_bounds(self) -> tuple[float, float, float, float]:
        """Get the bounds of the dataset, in EPSG:4326"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_dates(self) -> list[datetime.datetime]:
        raise NotImplementedError


# Used to lookup datasets by class name
_DATASET_CLASS_REGISTRY: dict[str, type[Dataset[Any]]] = {}


class _DatasetRegistry:
    """Factory creating instances of dataset subclasses based on an id and a a config"""

    def __init__(self) -> None:
        self._registry: dict[str, type[Dataset[Any]]] = {}

    def register_class(self, name: str, cls: type[Dataset[Any]]) -> None:
        if name in self._registry:
            raise ValueError(f"Name {name} already registered")
        if cls in self._registry.values():
            raise ValueError(f"Dataset class {cls} already registered")

        """Register a dataset class"""
        self._registry[name] = cls

    def unregister_class(self, name: str) -> None:
        """Unregister a dataset class"""
        if name not in self._registry:
            raise ValueError(f"Name {name} not registered")
        del self._registry[name]

    def get_registry_name(self, cls: type[Dataset[Any]]) -> str:
        for name, dataset_cls in self._registry.items():
            if dataset_cls == cls:
                return name
        raise ValueError(f"Dataset class {cls} is not registered")

    def create(
        self,
        name: str,
        dataset_name: str,
        metadata: DatasetMetadata,
        definition: dict[str, Any],
    ) -> Dataset[Any]:
        """Create a dataset instance"""
        if name not in self._registry:
            raise ValueError(f"Dataset class with name {name} not registered")
        cls = self._registry[name]
        return cls.from_serialized_definition(dataset_name, metadata, definition)


registry = _DatasetRegistry()
