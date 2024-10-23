import os
from typing import Any

import requests
from loguru import logger

from earthscale.api import DatasetRegistrationRequest
from earthscale.constants import (
    BACKEND_URL_ENV_VAR,
    DEFAULT_BACKEND_URL,
)
from earthscale.datasets.dataset import (
    Dataset,
    DatasetDomain,
    DatasetMetadata,
    registry,
)
from earthscale.repositories.utils import (
    timestamp_to_iso,
)
from supabase import Client

_DATASET_TABLE = "datasets"
_LATEST_DATASETS_TABLE = "datasets_latest"


class DatasetProcessingError(Exception):
    pass


class UserNotFoundError(Exception):
    pass


class NoOrganizationError(Exception):
    pass


class DatasetNotFoundError(Exception):
    pass


def get_org_id_for_user(
    client: Client,
    user_id: str,
) -> str:
    # This works because we have a policy that a user can only
    # view their own user info
    result = client.table("users").select("*").eq("id", user_id).execute()
    if result.data is None or len(result.data) == 0:
        raise UserNotFoundError(f"User {user_id} not found")
    org_id: str = result.data[0]["org_id"]
    if org_id is None:
        raise NoOrganizationError(f"User {user_id} has no organization")
    return org_id


class DatasetRepository:
    def __init__(
        self,
        client: Client,
        backend_url: str | None = None,
        domain: DatasetDomain | None = None,
        version: str | None = None,
    ):
        self.domain = domain
        self.version = version
        if backend_url is None:
            backend_url = os.getenv(BACKEND_URL_ENV_VAR)
        if backend_url is None:
            backend_url = DEFAULT_BACKEND_URL

        self._backend_url = backend_url.rstrip("/")

        if self.domain == DatasetDomain.WORKSPACE and version:
            raise ValueError("Cannot version a workspace dataset")

        self.client = client

    def get(
        self,
        id_: str,
    ) -> Dataset[Any]:
        query = (
            self.client.table(_DATASET_TABLE)
            .select("*")
            .eq("id", id_)
            .order("updated_at", desc=True)
        )
        if self.domain is not None:
            query = query.eq("domain", self.domain)
        if self.version:
            query = query.eq("version", self.version)
        results = query.limit(1).execute()
        if results.data is None or len(results.data) == 0:
            raise DatasetNotFoundError(f"No dataset found with id {id_}")
        dataset = self.raw_results_to_datasets(results.data)[0]
        return dataset

    def exists(
        self,
        name: str,
    ) -> bool:
        query = (
            self.client.table(_LATEST_DATASETS_TABLE)
            .select("*")
            .eq("name", name)
            .limit(1)
        )
        results = query.limit(1).execute()
        return results.data is not None and len(results.data) > 0

    def get_by_name(
        self,
        name: str,
    ) -> Dataset[Any]:
        query = (
            self.client.table(_LATEST_DATASETS_TABLE)
            .select("*")
            .eq("name", name)
            .order("updated_at", desc=True)
        )
        if self.domain is not None:
            query = query.eq("domain", self.domain)
        if self.version:
            query = query.eq("version", self.version)
        results = query.limit(1).execute()
        datasets = self.raw_results_to_datasets(results.data)
        if len(datasets) == 0:
            raise DatasetNotFoundError(f"No dataset found with name {name}")
        dataset = datasets[0]
        return dataset

    def get_all(
        self,
    ) -> list[Dataset[Any]]:
        query = (
            self.client.table(_DATASET_TABLE)
            .select("*")
            .order("updated_at", desc=True)
            .eq("domain", self.domain)
        )
        results = query.execute()
        datasets = self.raw_results_to_datasets(results.data)
        return datasets

    def get_recent(
        self,
        most_recent_timestamp: int,
    ) -> list[Dataset[Any]]:
        iso = timestamp_to_iso(most_recent_timestamp)
        query = (
            self.client.table(_DATASET_TABLE)
            .select("*")
            .gt("updated_at", iso)
            .eq("domain", self.domain)
            .order("updated_at", desc=True)
        )
        results = query.execute()
        datasets = self.raw_results_to_datasets(results.data)
        return datasets

    def add(
        self,
        dataset: Dataset[Any],
    ) -> None:
        data = DatasetRegistrationRequest(
            id=dataset.id,
            name=dataset.name,
            metadata=dataset.metadata,
            type=dataset.type,
            domain=self.domain,
            class_name=registry.get_registry_name(type(dataset)),
            dataset_definition=dataset.serialize_definition(),
        ).model_dump(mode="json")

        response = requests.post(
            f"{self._backend_url}/datasets/register",
            json=data,
            headers={
                "Authorization": f"Bearer {self.client.auth.get_session().access_token}"
            },
        )
        response.raise_for_status()

    def raw_results_to_datasets(
        self, results: list[dict[str, Any]]
    ) -> list[Dataset[Any]]:
        datasets = []
        seen_names = set()
        for result in results:
            if result["name"] in seen_names:
                continue
            try:
                dataset = registry.create(
                    result["class_name"],
                    result["name"],
                    DatasetMetadata(**result["metadata"]),
                    result["definition"],
                )

                datasets.append(dataset)
                seen_names.add(result["name"])
            except Exception as e:
                logger.error(f"Error loading dataset {result['name']}: {e}")
                raise e
        return datasets
