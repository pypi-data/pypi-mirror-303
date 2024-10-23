import abc
from dataclasses import asdict
from typing import Any

from earthscale_core.visualization import (
    BaseVisualizationParams,
    CategoricalVisualization,
    RGBVisualization,
    SingleBandVisualization,
    VectorVisualization,
    VectorVisualizationMode,
    Visualization,
    VisualizationType,
)
from supabase import Client

_VIZ_TABLE = "viz_params"


class AbstractVisualizationRepository(abc.ABC):
    @abc.abstractmethod
    def get_by_id(self, id_: str) -> Visualization:
        raise NotImplementedError

    @abc.abstractmethod
    def get_latest_by_dataset_name(self, name: str) -> Visualization:
        raise NotImplementedError

    @abc.abstractmethod
    def add(self, viz: Visualization) -> None:
        raise NotImplementedError


class VizNotFoundError(Exception):
    pass


def _unpack_viz_params(
    viz_type: VisualizationType, viz_params: dict[str, Any]
) -> BaseVisualizationParams:
    # Convert min-maxes per band to tuple as that's lost in serialization
    if "minMaxesPerBand" in viz_params:
        viz_params["minMaxesPerBand"] = {
            band: tuple(minMaxes)
            for band, minMaxes in viz_params["minMaxesPerBand"].items()
        }

    if viz_type == VisualizationType.VECTOR:
        return VectorVisualization(**viz_params)
    elif viz_type == VisualizationType.RGB:
        return RGBVisualization(**viz_params)
    elif viz_type == VisualizationType.SINGLE_BAND:
        return SingleBandVisualization(**viz_params)
    elif viz_type == VisualizationType.CATEGORICAL:
        # TODO: this is a hack to remove extra fields from the viz params
        viz_params_dict = {
            "valueMap": viz_params["valueMap"],
            "colorMap": viz_params["colorMap"],
        }
        return CategoricalVisualization(**viz_params_dict)
    else:
        raise ValueError(f"Unknown visualization type {viz_type}")


class SupabaseVisualizationRepository(AbstractVisualizationRepository):
    def __init__(
        self,
        client: Client,
    ):
        self._client = client

    def get_by_id(
        self,
        id_: str,
    ) -> Visualization:
        query = self._client.table(_VIZ_TABLE).select("*").eq("id", id_).limit(1)
        results = query.execute()

        if results.data is None or len(results.data) == 0:
            raise VizNotFoundError(f"No item found with id {id_}")

        data = results.data[0]
        viz_type = VisualizationType(data["type"])
        viz_params = data["params"]
        viz_params = _unpack_viz_params(viz_type, viz_params)
        viz = Visualization(
            id=data["id"],
            type=viz_type,
            params=viz_params,
            dataset_id=data["dataset_id"],
            created_at=data["created_at"],
            dataset_name=data["dataset_name"],
        )
        return viz

    def get_latest_by_dataset_name(self, name: str) -> Visualization:
        query = (
            self._client.table(_VIZ_TABLE)
            .select("*")
            .eq("dataset_name", name)
            .order("created_at", desc=True)
            .limit(1)
        )
        results = query.execute()

        if results.data is None or len(results.data) == 0:
            raise VizNotFoundError(f"No visualization found for dataset {name}")

        data = results.data[0]
        viz_type = VisualizationType(data["type"])
        viz_params = data["params"]
        viz_params = _unpack_viz_params(viz_type, viz_params)
        viz = Visualization(
            id=data["id"],
            type=viz_type,
            params=viz_params,
            dataset_id=data["dataset_id"],
            created_at=data["created_at"],
            dataset_name=data["dataset_name"],
        )
        return viz

    def add(self, viz: Visualization) -> None:
        viz_params = asdict(viz.params)
        for key, value in viz_params.items():
            # Hack, we should probably convert the visualization objects to Pydantic
            # models for better serialization support
            if isinstance(value, VectorVisualizationMode):
                viz_params[key] = value.value
        self._client.table(_VIZ_TABLE).insert(
            [
                {
                    "id": viz.id,
                    "dataset_id": viz.dataset_id,
                    "type": viz.type,
                    "params": viz_params,
                    "created_at": viz.created_at,
                    "dataset_name": viz.dataset_name,
                }
            ]
        ).execute()
