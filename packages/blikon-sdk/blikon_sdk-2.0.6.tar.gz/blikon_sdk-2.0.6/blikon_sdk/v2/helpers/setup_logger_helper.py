import logging
import time
from blikon_sdk.v2.models.sdk_configuration_model import SDKConfiguration
from opencensus.ext.azure.log_exporter import AzureLogHandler


def _setup_sdk_logger(sdk_configuration: SDKConfiguration) -> None:
    """
    Configure and set up the logger for the SDK
    :param sdk_configuration: The data required for setting up the SDK logger
    :return: None
    """
    # Deactivate logs from server
    # logging.getLogger("uvicorn.error").disabled = True
    # logging.getLogger("uvicorn.access").disabled = True
    # logging.getLogger("fastapi").disabled = True
    # logging.getLogger("starlette").disabled = True

    # Get a logger with a unique name
    logger = logging.getLogger(sdk_configuration.sdk_settings.logger_name)
    # Disable root propagation
    logger.propagate = False
    # Set the global logger level
    logger.setLevel(sdk_configuration.sdk_settings.logging_level_console)
    # Create the formatter for correct display in terminal
    formatter = _CustomFormatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Configure the logger for terminal
    if sdk_configuration.sdk_settings.log_to_console:
        try:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(
                sdk_configuration.sdk_settings.logging_level_console
            )
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
        except Exception as exc:
            raise RuntimeError("Failed to initialize the log console handler") from exc

    # Configure the logger for file logging
    if sdk_configuration.sdk_settings.log_to_file:
        try:
            file_handler = logging.FileHandler(
                sdk_configuration.sdk_settings.logging_file_name
            )
            file_handler.setLevel(sdk_configuration.sdk_settings.logging_level_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except Exception as exc:
            raise RuntimeError("Failed to initialize the log file handler") from exc

    # Configure the logger for Azure Application Insights logging
    if sdk_configuration.sdk_settings.log_to_azure:
        try:
            azure_log_handler = AzureLogHandler(
                connection_string="InstrumentationKey="
                + sdk_configuration.sdk_settings.azure_insights_instrumentation_key
            )
            azure_log_handler.setLevel(
                sdk_configuration.sdk_settings.logging_level_azure_insights
            )
            azure_log_handler.setFormatter(formatter)
            logger.addHandler(azure_log_handler)
        except Exception as exc:
            raise RuntimeError(
                "Failed to initialize the Azure Application Insights log handler"
            ) from exc


class _CustomFormatter(logging.Formatter):
    """
    Custom formatter that formats logging messages
    """

    def formatTime(self, record, datefmt=None):
        ct = time.localtime(record.created)
        if datefmt:
            return time.strftime(datefmt, ct)
        else:
            # Format the time with milliseconds, ensuring three digits
            return f"{time.strftime('%Y-%m-%d %H:%M:%S', ct)}.{int(record.msecs):03d}"
