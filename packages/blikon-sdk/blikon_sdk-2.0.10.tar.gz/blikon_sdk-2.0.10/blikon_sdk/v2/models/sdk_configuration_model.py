from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv


# Load .env variables
load_dotenv()  # '.env' file or similar must exist (root folder or Azure .env variables)


class _EnvSettings(BaseSettings):
    """
    .env configuration goes here
    """

    API_USER: str = "user"
    API_USER_PASSWORD: str = "password"
    JWT_SECRET: str = "your_jwt_secret"
    JWT_EXPIRATION_TIME_MINUTES: int = 30
    CONTINGENCY_SERVICE_URL: str = ""
    PYTHON_TOKEN: str = ""

    class Config:
        env_file = (
            ".env"  # Make sure to put .env variables in this file (or Azure section)
        )
        env_prefix = "SDK_"  # Prefix used for SDK .env variables (make sure to use it)
        extra = "allow"  # Allow additional variables (App .env variables for instance)


class _BaseSDKConfiguration(BaseModel):
    """
    Required basic SDK configuration goes here
    """

    sdk_creator: str = "Raúl Díaz Peña"
    sdk_name: str = "SDK for Python FastAPI development, created by Raúl Díaz Peña"
    sdk_version: str = "2.0.10"
    jwt_algorithm: str = "HS256"
    http_timeout_sec: int = 10
    http_connect_sec: int = 5
    logger_name: str = "SDK_logger"


class _SDKSettings(_BaseSDKConfiguration):
    """
    Required (from client) configuration goes here
    """

    client_application_name: str = ""
    client_application_description: str = ""
    client_application_version: str = ""
    client_application_mode: int = 2
    client_application_language: str = "es"  # ["es", "en", "fr", "de", "pt"]
    client_application_contingency_id: str = ""
    log_to_console: bool = False
    log_to_file: bool = False
    log_to_azure: bool = False
    logging_level_console: int = 20  # INFO, WARNING, ERROR, CRITICAL
    logging_level_file: int = 20  # INFO, WARNING, ERROR, CRITICAL
    logging_level_azure_insights: int = 20  # INFO, WARNING, ERROR, CRITICAL
    logging_file_name: str = "app.log"
    azure_insights_instrumentation_key: str = (
        ""  # Application Insights key (for logging into Azure)
    )
    azure_insights_avoid_404_log: bool = (
        False  # Avoid to log requests from endpoints not found
    )


class SDKConfiguration(BaseModel):
    """
    Main SDK Configuration class to be used
    """

    sdk_settings: _SDKSettings = _SDKSettings()
    env_settings: _EnvSettings = _EnvSettings()
