import httpx
from blikon_sdk.v2.core.core import Core
from blikon_sdk.v2.models.sdk_client_setup_model import SDKClientSetupSettings
from blikon_sdk.v2.models.sdk_configuration_model import SDKConfiguration
from blikon_sdk.v2.helpers.setup_logger_helper import _setup_sdk_logger
from blikon_sdk.v2.services.log_service import LogService
from blikon_sdk.v2.services.security_service import SecurityService


def setup_core(
    client_sdk_settings: SDKClientSetupSettings, client_app_settings
) -> None:
    _setup_sdk_configuration(client_sdk_settings)
    _setup_app_configuration(client_app_settings)
    _setup_logger()
    _setup_httpx_client()
    _setup_log_service()
    _setup_security_service()
    _log_succesfull_setup()


def _setup_sdk_configuration(client_sdk_settings: SDKClientSetupSettings) -> None:
    """
    Sets up the specific SDK configuration data to satisfy model 'SDKConfiguration'
    It also adds the 'SDKConfiguration' object to the core
    :param client_sdk_settings: The required client configuration data
    :return: None
    """
    try:
        sdk_configuration: SDKConfiguration = SDKConfiguration()
        sdk_configuration.sdk_settings = sdk_configuration.sdk_settings.copy(
            update=client_sdk_settings.dict()
        )
        Core.set_sdk_configuration(sdk_configuration)
    except Exception as exc:
        raise RuntimeError("Failed to initialize SDK Configuration") from exc


def _setup_app_configuration(client_app_settings) -> None:
    """
    Sets up the specific App configuration data provided by the client
    It also adds the object to the core as 'app_configuration'
    :param client_app_settings: The App configuration object provided by the client
    :return: None
    """
    try:
        Core.set_app_configuration(client_app_settings)
    except Exception as exc:
        raise RuntimeError("Failed to initialize client App Configuration") from exc


def _setup_logger() -> None:
    """
    Sets up the logger and gets it ready for use
    :return: None
    """
    try:
        sdk_config = Core.get_sdk_configuration()
        _setup_sdk_logger(sdk_config)
    except Exception as exc:
        raise RuntimeError("Failed to initialize Logging Configuration") from exc


def _setup_httpx_client() -> None:
    """
    Sets up the Httpx Client and adds it to the core as a singleton instance
    :return: None
    """
    try:
        sdk_config: SDKConfiguration = Core.get_sdk_configuration()
        httpx_client: httpx.AsyncClient = httpx.AsyncClient(
            timeout=httpx.Timeout(
                sdk_config.sdk_settings.http_timeout_sec,
                connect_timeout=sdk_config.sdk_settings.http_connect_sec,
            )
        )
        Core.set_httpx_client(httpx_client)
    except Exception as exc:
        raise RuntimeError("Failed to initialize the Httpx Client") from exc


def _setup_log_service() -> None:
    """
    Sets up the Log Service and adds it to the core as a singleton instance
    :return: None
    """
    try:
        sdk_config = Core.get_sdk_configuration()
        log_service: LogService = LogService(sdk_config.sdk_settings.logger_name)
        Core.set_log_service(log_service)
    except Exception as exc:
        raise RuntimeError("Failed to initialize Log Service") from exc


def _setup_security_service() -> None:
    """
    Sets up the Security Service and adds it to the core as a singleton instance
    :return: None
    """
    try:
        sdk_config = Core.get_sdk_configuration()
        security_service: SecurityService = SecurityService(sdk_config)
        Core.set_security_service(security_service)
    except Exception as exc:
        raise RuntimeError("Failed to initialize Security Service") from exc


def _log_succesfull_setup() -> None:
    # Log first info, regarding successfully setting up the SDK
    sdk_config = Core.get_sdk_configuration()
    log_service = Core.get_log_service()
    log_service.info(f"{log_service.get_special_line()}")
    log_service.info(
        f"Blikon SDK version {sdk_config.sdk_settings.sdk_version} has been successfully configured, created by {sdk_config.sdk_settings.sdk_creator}."
    )
    log_service.info(f"{log_service.get_special_line()}")
    log_service.info(f"{log_service.get_line()}")
    log_service.info(f"Use the 'Core' class to get all the singleton instances:")
    log_service.info(f"• get_sdk_configuration()")
    log_service.info(f"• get_app_configuration()")
    log_service.info(f"• get_httpx_client()")
    log_service.info(f"• get_log_service()")
    log_service.info(f"• get_security_service()")
    log_service.info(
        f"Importing the 'Core': 'from blikon_sdk.v2.core.core import Core'"
    )
    log_service.info(f"{log_service.get_line()}")
    log_service.info(f"{log_service.get_line()}")
    log_service.info(f"Add the following SDK middleware to your FastAPI app main file:")
    log_service.info(
        f"• ErrorHandlingMiddleware, used as follows: 'ErrorHandlingMiddleware(app)'"
    )
    log_service.info(
        f"• HttpLoggingMiddleware, used as follows: 'app.add_middleware(HttpLoggingMiddleware)'"
    )
    log_service.info(
        f"Importing the error handler: 'from blikon_sdk.v2.middleware.error_handler import ErrorHandlingMiddleware'"
    )
    log_service.info(
        f"Importing the log handler: 'from blikon_sdk.v2.middleware.http_logger import HttpLoggingMiddleware'"
    )
    log_service.info(f"{log_service.get_line()}")
    log_service.info(f"{log_service.get_line()}")
    log_service.info(
        "Use the 'msg' function to deliver messages in the application's specified language."
    )
    log_service.info(
        f"Importing the 'msg' function: 'from blikon_sdk.v2.helpers.msg_helper import msg'"
    )
    log_service.info(f"{log_service.get_line()}")
