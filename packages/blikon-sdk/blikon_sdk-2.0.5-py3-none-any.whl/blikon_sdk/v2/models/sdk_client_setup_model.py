from pydantic import BaseModel


class SDKClientSetupSettings(BaseModel):
    """
    Required (from client) configuration goes here
    """

    client_application_name: str = ""
    client_application_description: str = ""
    client_application_version: str = ""
    client_application_mode: int = 2
    client_application_language: str = "en"
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
