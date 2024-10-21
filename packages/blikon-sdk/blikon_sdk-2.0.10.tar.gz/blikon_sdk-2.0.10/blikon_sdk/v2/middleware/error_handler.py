import traceback, os
import httpx
from pydantic import ValidationError
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException, RequestValidationError
from typing import List, Dict, Any
from blikon_sdk.v2.schemas.shared_schemas import ErrorResponse
from blikon_sdk.v2.models.error_detail_model import ErrorDetail
from blikon_sdk.v2.utils.utils import DateTimeUtil
from blikon_sdk.v2.core.core import Core
from blikon_sdk.v2.helpers.msg_helper import msg
from blikon_sdk.v2.schemas.critical_error_schemas import CriticalError


class ErrorHandlingMiddleware:
    def __init__(self, app: FastAPI):
        self.app = app
        self.sdk_configuration = Core.get_sdk_configuration()
        self.log_service = Core.get_log_service()
        self.setup()

    def setup(self):
        @self.app.exception_handler(RequestValidationError)
        @self.app.exception_handler(ValidationError)
        async def validation_exception_handler(
            request: Request, exc: Exception
        ) -> JSONResponse:
            validation_errors = None
            detail = (
                "Validation error"  # Mensaje genérico para los errores de validación
            )
            if isinstance(exc, (RequestValidationError, ValidationError)):
                validation_errors = self._format_and_clean_validation_errors(
                    exc.errors()
                )
            else:
                detail = "Internal validation error"
            return await self._handleError(422, request, detail, exc, validation_errors)

        @self.app.exception_handler(HTTPException)
        async def handle_http_exception(
            request: Request, exc: HTTPException
        ) -> JSONResponse:
            status_code = exc.status_code
            detail = str(exc.detail)
            if exc.status_code == 403:
                status_code = 401
                detail = "Unauthorized"
            return await self._handleError(status_code, request, detail, exc)

        @self.app.exception_handler(Exception)
        async def handle_exception(request: Request, exc: Exception) -> JSONResponse:
            validation_errors = None
            if isinstance(exc, ValidationError):
                validation_errors = self._format_and_clean_validation_errors(
                    exc.errors()
                )
                message = "Validation error"
            else:
                message = "Internal server error"
            return await self._handleError(
                500, request, message, exc, validation_errors
            )

    async def _handleError(
        self,
        status_code: int,
        request: Request,
        message: str,
        exc,
        validation_errors=None,
    ) -> JSONResponse:
        file_name, function_name, line_number = self._get_traceback_details(exc)

        error_detail = ErrorDetail(
            client_application_name=self.sdk_configuration.sdk_settings.client_application_name,
            client_application_version=self.sdk_configuration.sdk_settings.client_application_version,
            client_application_mode=self.sdk_configuration.sdk_settings.client_application_mode,
            datetime=DateTimeUtil.get_datetime_now(),
            exception_type=type(exc).__name__,
            error_message=str(exc),
            file_name=file_name,
            function_name=function_name,
            line_number=line_number,
            endpoint=str(request.url.path),
            status_code=status_code,
            validation_errors=validation_errors,
        )
        error_response = ErrorResponse(
            result=False,
            message=msg(message),
            exception_type=error_detail.exception_type,
            validation_errors=validation_errors,
        )

        # Log the error
        self.log_service.error_info(error_detail)

        # Report the error to the 'Contingency Service' only if it is critical (500-599)
        if 500 <= error_detail.status_code < 600:
            # Get the traceback as string
            tb_str = "".join(
                traceback.format_exception(type(exc), exc, exc.__traceback__)
            )
            # Limit the traceback to a certain number of lines (e.g., last 10 lines)
            max_lines = 20
            tb_str_limited = "\n".join(tb_str.splitlines()[-max_lines:])
            await self._report_error(error_detail, tb_str_limited, request.method)

        return JSONResponse(
            status_code=status_code, content=error_response.model_dump()
        )

    def _get_traceback_details(self, exc: Exception) -> (str, str, int):
        file_name = "unknown"
        function_name = "unknown"
        line_number = -1
        try:
            tb = exc.__traceback__
            tb_frame = traceback.extract_tb(tb)[-1]
            file_name = os.path.basename(tb_frame.filename)
            function_name = tb_frame.name
            line_number = tb_frame.lineno
        except Exception:
            pass
        return file_name, function_name, line_number

    def _format_and_clean_validation_errors(
        self, validation_errors: List[Dict[str, Any]]
    ) -> List[Dict[str, str]]:
        formatted_errors = []
        for error in validation_errors:
            field = ".".join(str(loc) for loc in error.get("loc", []))
            field = field.replace("body.", "")
            message = error.get("msg", "Unknown error")
            if message.startswith("Value error, "):
                message = message[len("Value error, ") :]
            formatted_errors.append({"field": field, "message": msg(message)})
        return formatted_errors

    async def _report_error(
        self, error_detail: ErrorDetail, traceback: str, method: str
    ) -> None:
        try:
            # Set the criticality level
            criticality: int = 3
            match error_detail.status_code:
                case 500:
                    criticality = 1
                case 503:
                    criticality = 2

            debugged_error_message = error_detail.error_message
            # Validate length and truncate if necessary
            if len(debugged_error_message) > 300:
                debugged_error_message = debugged_error_message[:300]

                # Create the schema object for the 'Contingency Service'
            critical_error: CriticalError = CriticalError(
                client_application_id=self.sdk_configuration.sdk_settings.client_application_contingency_id,
                exception_type=error_detail.exception_type,
                error_message=debugged_error_message,
                criticality=criticality,
                traceback=traceback,
                file_name=error_detail.file_name,
                function_name=error_detail.function_name,
                line_number=error_detail.line_number,
                endpoint=error_detail.endpoint,
                method=method,
                status_code=error_detail.status_code,
                additional_info={"logged_by": "blikon_sdk"},
            )

            # Prepare headers and url for the request
            headers = {
                "authorization": f"Bearer {self.sdk_configuration.env_settings.PYTHON_TOKEN}"
            }
            base_url = self.sdk_configuration.env_settings.CONTINGENCY_SERVICE_URL
            relative_url = f"/v1/errors"

            # Make the request to log the error
            client = Core.get_httpx_client()
            api_response = await client.post(
                f"{base_url}{relative_url}", headers=headers, json=critical_error.dict()
            )

            # Check the response and log the result
            if api_response.status_code == 200:
                self.log_service.info(
                    "Critical error succesfully logged into the Contingency Service",
                    source="blikon_sdk",
                    function="_report_error",
                )
            else:
                self.log_service.error(
                    f"Failed to log error into the Contingency Service. Status code: {api_response.status_code}. Response: {api_response.text}",
                    source="blikon_sdk",
                    function="_report_error",
                )
                raise HTTPException(
                    status_code=api_response.status_code,
                    detail=f"The SDK was not able to log the critical error. Response: {api_response.text}",
                )
        except Exception as e:
            self.log_service.error(
                f"Unable to log error into the Contingency Service. Error message: {str(e)}",
                source="blikon_sdk",
                function="_report_error",
            )
