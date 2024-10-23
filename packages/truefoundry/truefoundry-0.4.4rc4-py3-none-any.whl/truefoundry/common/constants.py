import os
from pathlib import Path
from typing import Optional

from truefoundry.pydantic_v1 import BaseSettings, Field, SecretStr

TFY_CONFIG_DIR = Path.home() / ".truefoundry"
CREDENTIAL_FILEPATH = TFY_CONFIG_DIR / "credentials.json"

# These keys are kept separately because we use them in error messages and some checks
TFY_HOST_ENV_KEY = "TFY_HOST"
TFY_API_KEY_ENV_KEY = "TFY_API_KEY"


class TrueFoundrySdkEnv(BaseSettings):
    # Note: Every field in this class should have a default value
    # Never expect the user to set these values
    TFY_HOST: Optional[str] = Field(default=None, env=TFY_HOST_ENV_KEY)
    TFY_API_KEY: Optional[SecretStr] = Field(default=None, env=TFY_API_KEY_ENV_KEY)
    TFY_ARTIFACTS_DOWNLOAD_CHUNK_SIZE_BYTES: int = 100 * 1000 * 1000
    TFY_ARTIFACTS_DOWNLOAD_MAX_WORKERS: int = max(min(32, (os.cpu_count() or 2) * 2), 4)
    TFY_ARTIFACTS_UPLOAD_MAX_WORKERS: int = max(min(32, (os.cpu_count() or 2) * 2), 4)
    TFY_ARTIFACTS_DISABLE_MULTIPART_UPLOAD: bool = False
    TFY_ARTIFACTS_DOWNLOAD_FSYNC_CHUNKS: bool = False
    TFY_CLI_LOCAL_DEV_MODE: bool = False
    TFY_PYTHONBUILD_PYTHON_IMAGE_REPO: str = "public.ecr.aws/docker/library/python"


ENV_VARS = TrueFoundrySdkEnv()
API_SERVER_RELATIVE_PATH = "api/svc"
MLFOUNDRY_SERVER_RELATIVE_PATH = "api/ml"
VERSION_PREFIX = "v1"
SERVICEFOUNDRY_CLIENT_MAX_RETRIES = 2
