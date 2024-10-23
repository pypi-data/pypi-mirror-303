from earthscale.types import Chunksizes

BACKEND_URL_ENV_VAR = "EARTHSCALE_BACKEND_URL"
DEFAULT_BACKEND_URL = "https://backend.earthscale.ai/api"

NUM_CHUNKS_FOR_MIN_MAX_ESTIMATION = 5

# Kind of arbitrary, but we don't want to estimate min/max for too many bands
MAX_NUM_BANDS_FOR_MIN_MAX_ESTIMATION = 64

XARRAY_CACHE_LEN = 64

DEFAULT_CHUNKSIZES: Chunksizes = {"x": 1024, "y": 1024, "time": 1}

MAX_NUM_EO_ASSET_BANDS = 100

METERS_PER_DEGREE = 111_319.9
