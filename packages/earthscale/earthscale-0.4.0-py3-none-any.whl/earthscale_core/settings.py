from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

import earthscale_core

_ENV_FILE = Path(earthscale_core.__file__).parent.parent / ".env"


class Settings(BaseSettings):
    # Locally: All settings will come from ./.env
    # Remote: General setting come from environment variables
    model_config = SettingsConfigDict(
        env_prefix="EARTHSCALE_",
        # For the local development case
        env_file=_ENV_FILE,
        extra="ignore",
    )

    supabase_url: str
    supabase_anon_key: str

    backend_url: str

    # When a user adds a vector dataset, we convert the vector data to flatgeobuf
    # for faster visualization. These flatgeobuf files will be saved in
    # <vector_tile_prefix>/<dataset_id>/converted.fgb
    # Can either be a local path or a cloud storage prefix
    vector_tile_prefix: str

    stac_item_repository_root: str = ""

    # Required by the fronted and we don't allow extra arguments in the settings right
    # now
    mapbox_token: str = ""
