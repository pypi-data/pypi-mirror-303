from dataclasses import dataclass
from enum import Enum


class VectorVisualizationMode(Enum):
    FILL = "fill"
    OUTLINE = "outline"


@dataclass
class BaseVisualizationParams:
    pass


@dataclass
class BaseRasterVisualizationParams(BaseVisualizationParams):
    pass


@dataclass
class VectorVisualization(BaseVisualizationParams):
    mode: VectorVisualizationMode
    color: str
    width: int | None = None


@dataclass
class SingleBandVisualization(BaseRasterVisualizationParams):
    minMaxesPerBand: dict[str, tuple[float, float]] | None
    band: str
    # TODO: change naming convention in db push from frontend
    colorRamp: str | None = None
    min: float | None = None
    max: float | None = None


@dataclass
class RGBVisualization(BaseRasterVisualizationParams):
    minMaxesPerBand: dict[str, tuple[float, float]] | None
    red: str
    green: str
    blue: str


@dataclass
class CategoricalVisualization(BaseRasterVisualizationParams):
    valueMap: dict[str, int] | dict[str, list[int]]
    colorMap: str


class VisualizationType(str, Enum):
    SINGLE_BAND = "continuous_singleband_raster"
    RGB = "continuous_multiband_raster"
    VECTOR = "vector"
    CATEGORICAL = "categorical_raster"


@dataclass
class Visualization:
    id: str
    type: VisualizationType
    params: BaseVisualizationParams
    dataset_id: str
    created_at: str
    dataset_name: str
