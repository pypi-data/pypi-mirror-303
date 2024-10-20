import json
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from typing import Callable
from blikon_sdk.v2.models.http_log_model import HttpLog
from blikon_sdk.v2.services.log_service import LogService
from blikon_sdk.v2.utils.utils import DateTimeUtil
from blikon_sdk.v2.core.core import Core


class HttpLoggingMiddleware(BaseHTTPMiddleware):
    """
    The middleware class that handles HTTP logging requests and responses
    """

    IGNORED_ENDPOINTS = ["/docs", "/openapi.json"]

    def __init__(self, app):
        super().__init__(app)
        self.sdk_configuration = Core.get_sdk_configuration()
        self.log_service: LogService = Core.get_log_service()

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """
        This function intercepts every http call and logs the request
        :param request: The starlette request object
        :param call_next: The function to call next
        :return: The starlette response object
        """
        start_datetime = DateTimeUtil.get_datetime_now()
        user_agent = request.headers.get("user-agent", "")
        os_info, browser = self._parse_user_agent(user_agent)

        # Read the request body
        body = await request.body()

        # Process request
        response: Response = await call_next(request)

        # Process the response body
        response_body = b""
        async for chunk in response.body_iterator:
            response_body += chunk

        # Get time data and intervals
        end_datetime = DateTimeUtil.get_datetime_now()
        process_time = end_datetime - start_datetime
        status_code = response.status_code

        # Get the request and response bodies
        MAX_LOG_BODY_SIZE = 1000
        request_body_clean = self._get_request_body(body)[:MAX_LOG_BODY_SIZE]
        response_body_clean = self._get_response_body(response_body)[:MAX_LOG_BODY_SIZE]

        # Build the http call log
        http_log = HttpLog(
            endpoint=request.url.path,
            method=request.method,
            start_time=DateTimeUtil.get_datetime_str(start_datetime),
            client_ip=request.client.host,
            real_client_ip=self._get_real_client_ip(request),
            user_agent=user_agent,
            operating_system=os_info,
            browser=browser,
            request_params=str(request.query_params),
            request_body=request_body_clean,
            end_time=DateTimeUtil.get_datetime_str(end_datetime),
            duration=f"{process_time.total_seconds():.4f}",
            status_code=str(status_code),
            response_body=response_body_clean,
        )

        # Flag to determine logging the http call
        flag_log_call = True

        # Check if status code is 404
        if http_log.status_code == "404":
            if self.sdk_configuration.sdk_settings.azure_insights_avoid_404_log:
                flag_log_call = False

        # Check if endpoint should be ignored
        if http_log.endpoint in self.IGNORED_ENDPOINTS:
            flag_log_call = False

        if flag_log_call:
            # Log the http call
            self.log_service.http_info(http_log)

        # Reconstruct the response with the original body
        return Response(
            content=response_body,
            status_code=status_code,
            headers=dict(response.headers),
        )

    def _get_request_body(self, body: bytes) -> str:
        request_body_str = None
        try:
            request_body_str = body.decode("utf-8")
            # Try to ge the json and then put it in a clean string
            request_body_json = json.loads(request_body_str)
            request_body_clean = json.dumps(
                request_body_json, separators=(",", ":"), ensure_ascii=False
            )
        except (json.JSONDecodeError, UnicodeDecodeError):
            # Keep the body raw if failure
            request_body_clean = request_body_str
        return request_body_clean

    def _get_response_body(self, response_body: bytes) -> str:
        try:
            response_body_str = response_body.decode("utf-8")
            # Try to get a clean json
            try:
                response_body_json = json.loads(response_body_str)
                response_body_clean = json.dumps(
                    response_body_json, separators=(",", ":"), ensure_ascii=False
                )
            except json.JSONDecodeError:
                # If not json, keep the body
                response_body_clean = response_body_str
        except UnicodeDecodeError:
            response_body_clean = ""
        return response_body_clean

    def _get_real_client_ip(self, request: Request) -> str:
        forwarded_for = request.headers.get("x-forwarded-for")
        if forwarded_for:
            # Verifies that the IP address is valid
            real_ip = forwarded_for.split(",")[0].strip()
            if real_ip:
                return real_ip
        return request.client.host

    def _parse_user_agent(self, user_agent: str):
        os_info = "Unknown OS"
        browser_info = "Unknown Browser"

        # Simple regex patterns (can be improved)
        os_patterns = {
            "Windows": "Windows",
            "Macintosh": "Mac OS",
            "Linux": "Linux",
            "Android": "Android",
            "iPhone": "iOS",
        }

        browser_patterns = {
            "Firefox": "Firefox",
            "Chrome": "Chrome",
            "Safari": "Safari",
            "MSIE": "Internet Explorer",
            "Trident": "Internet Explorer",
        }

        for key, value in os_patterns.items():
            if key in user_agent:
                os_info = value
                break

        for key, value in browser_patterns.items():
            if key in user_agent:
                browser_info = value
                break

        return os_info, browser_info
