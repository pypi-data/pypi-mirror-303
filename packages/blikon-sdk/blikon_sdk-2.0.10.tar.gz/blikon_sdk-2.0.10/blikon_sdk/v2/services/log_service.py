import logging
from blikon_sdk.v2.models.http_log_model import HttpLog
from blikon_sdk.v2.models.error_detail_model import ErrorDetail
from blikon_sdk.v2.utils.utils import DateTimeUtil


sep = " | "
line = "----------------------------------------------------------------------------------------------------"
special_line = "****************************************************************************************************"


class LogService:
    """
    This class provides logging service
    """

    def __init__(self, logger_name) -> None:
        # Get the SDK logger ready for use
        self.logger = logging.getLogger(logger_name)

    def get_line(self):
        """
        :return: The line of a 100 '-'
        """
        return line

    def get_special_line(self):
        """
        :return: The special line of a 100 '*'
        """
        return special_line

    def info(self, text: str, **kwargs) -> None:
        """
        Log some info using the configured logger handlers
        :param text: The text to be logged
        :param kwargs: Additional data
        :return: None
        """
        # Form a chain from kwargs
        kwargs_string = f"{sep}".join(
            f"{key}='{value}'" for key, value in kwargs.items()
        )
        # Concatenate the original text with the kwargs
        message = f"{text}{sep}{kwargs_string}" if kwargs else text
        self.logger.info(message)

    def error(self, text: str, **kwargs) -> None:
        """
        Log some error info using the configured logger handlers
        :param text: The text to be logged
        :param kwargs: Additional data
        :return: None
        """
        # Form a chain from kwargs
        kwargs_string = f"{sep}".join(
            f"{key}='{value}'" for key, value in kwargs.items()
        )
        # Concatenate the original text with the kwargs
        message = f"{text}{sep}{kwargs_string}" if kwargs else text
        self.logger.error(message)

    def error_info(self, error_detail: ErrorDetail) -> None:
        """
        Log the error detail using the configured logger handlers
        :param error_detail: a model with the error detail
        :return: None
        """
        self.error(f"{line}")
        self.error(f"Client Application Name: '{error_detail.client_application_name}'")
        self.error(
            f"Client Application Version: '{error_detail.client_application_version}'"
        )
        self.error(f"Client Application Mode: '{error_detail.client_application_mode}'")
        self.error(
            f"Datetime: '{DateTimeUtil.get_datetime_str(error_detail.datetime)}'"
        )
        self.error(f"Exception Type: '{error_detail.exception_type}'")
        self.error(f"Error Message: '{error_detail.error_message}'")
        self.error(f"File Name: '{error_detail.file_name}'")
        self.error(f"Function Name: '{error_detail.function_name}'")
        self.error(f"Line Number: '{error_detail.line_number}'")
        self.error(f"Endpoint: '{error_detail.endpoint}'")
        self.error(f"Status Code: '{error_detail.status_code}'")
        self.error(f"Validation Errors: '{error_detail.validation_errors}'")
        self.error(f"{line}")
        self._handleErrorLog()

    def http_info(self, http_log: HttpLog) -> None:
        """
        Log the http request-response detail using the configured logger handlers
        :param http_log: the model with the http detail
        :return: None
        """
        self.info(f"{line}")
        self.info(f"Starting Time: '{http_log.start_time}'")
        self.info(
            f"IP: '{http_log.client_ip}'{sep}IO: '{http_log.operating_system}'{sep}Browser: '{http_log.browser}'"
        )
        self.info(f"Endpoint: '{http_log.endpoint}'")
        self.info(f"Status Code: '{http_log.status_code}'")
        self.info(f"Request params: '{http_log.request_params}'")
        self.info(f"Request body: '{http_log.request_body}'")
        self.info(f"Response: '{http_log.response_body}'")
        self.info(f"Duration: '{http_log.duration} sec'")
        self.info(f"Ending Time: '{http_log.end_time}'")
        self.info(f"{line}")

    def service_info(self, service_name: str, function_name: str, **kwargs) -> None:
        """
        Logs some data that comes from a specific service
        :param service_name: The name of the service
        :param function_name: The name of the service function
        :param kwargs: The data to log
        :return: None
        """
        kwargs_str = ", ".join([f"{key}='{value}'" for key, value in kwargs.items()])
        self.info(f"{line}")
        self.info(
            f"Service: '{service_name}'{sep}Function: '{function_name}'{sep}{kwargs_str}"
        )
        self.info(f"{line}")

    def service_error(self, service_name: str, function_name: str, **kwargs) -> None:
        """
        Logs error data that comes from a specific service
        :param service_name: The name of the service
        :param function_name: The name of the service function
        :param kwargs: The data to log
        :return: None
        """
        kwargs_str = ", ".join([f"{key}='{value}'" for key, value in kwargs.items()])
        self.error(f"{line}")
        self.error(
            f"Service: '{service_name}'{sep}Function: '{function_name}'{sep}{kwargs_str}"
        )
        self.error(f"{line}")

    def service_request_info(
        self, service_name: str, function_name: str, json: str
    ) -> None:
        """
        Logs the JSON request that comes from a specific service
        :param service_name: Name of the service
        :param function_name: Name of the service function
        :param json: The json request to log
        :return: None
        """
        self.info(f"{line}")
        self.info(
            f"Service: '{service_name}'{sep}Function: '{function_name}'{sep}Request: '{json}'"
        )
        self.info(f"{line}")

    def service_response_info(
        self, service_name: str, function_name: str, status_code: int, json: str
    ) -> None:
        """
        Logs the json response that comes from a specific service
        :param service_name: Name of the service
        :param function_name: Name of the service function
        :param status_code: The status code of the response
        :param json: The json response to log
        :return: None
        """
        self.info(f"{line}")
        self.info(
            f"Service: '{service_name}'{sep}Function: '{function_name}'{sep}Status Code: '{status_code}'{sep}Response: '{json}'"
        )
        self.info(f"{line}")

    def _handleErrorLog(self):
        # Send error alert
        # Create and use new helper for this function
        pass
