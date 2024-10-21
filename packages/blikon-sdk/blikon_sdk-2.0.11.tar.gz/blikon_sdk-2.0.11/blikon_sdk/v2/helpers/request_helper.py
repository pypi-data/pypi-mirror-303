import httpx
from fastapi import HTTPException
from typing import Literal, Dict, Optional
from blikon_sdk.v2.services.log_service import LogService
from blikon_sdk.v2.core.core import Core


async def make_request(
    httpx_client: httpx.AsyncClient,
    method: Literal["get", "post", "put", "patch", "delete"],
    base_url: str,
    relative_url: str,
    message_503: str,
    json_data: Optional[Dict] = None,
    params: Optional[Dict] = None,
    token: Optional[str] = None,
    service_name: Optional[str] = None,
    function_name: Optional[str] = None,
) -> dict:
    """
    Make an HTTP request using httpx.

    :param httpx_client: The httpx client instance.
    :param method: The HTTP method to use.
    :param base_url: The base URL of the API.
    :param relative_url: The relative URL to append to the base URL.
    :param message_503: Message to use in case of a 503 error.
    :param json_data: JSON data to send in the body (for POST, PUT, PATCH).
    :param params: Query parameters to include in the URL.
    :param token: Optional authorization token.
    :param service_name: Optional service name for logging.
    :param function_name: Optional function name for logging.
    :return: The JSON response as a dictionary.
    """

    # Get the Log Service
    log_service: LogService = Core.get_log_service()

    # Set headers
    headers = {"Authorization": f"Bearer {token}"} if token else {}

    # Log the json data for information:
    if json_data is not None:
        log_service.service_info(
            service_name=service_name,
            function_name=function_name,
            request_json=json_data,
        )

    # Log the params data for information:
    if params is not None:
        log_service.service_info(
            service_name=service_name,
            function_name=function_name,
            request_params=params,
        )

    try:
        # Choose the appropriate request method
        if method in {"post", "put", "patch"}:
            response = await httpx_client.request(
                method,
                f"{base_url}{relative_url}",
                headers=headers,
                json=json_data,
                params=params,
            )
        elif method in {"get", "delete"}:
            response = await httpx_client.request(
                method, f"{base_url}{relative_url}", headers=headers, params=params
            )
        else:
            raise ValueError(f"Unsupported method: {method}")

        # Raise an error for HTTP error codes
        response.raise_for_status()

        # Try to get the JSON response
        try:
            json_response = response.json()
            if not json_response:
                raise ValueError("Empty JSON response")
            # Log the response information
            log_service.service_info(
                service_name=service_name,
                function_name=function_name,
                status_code=response.status_code,
                response_json=json_response,
            )
            return json_response
        except ValueError:
            raise ValueError("Response is not valid JSON")

    except httpx.HTTPStatusError as http_err:
        # Log and raise HTTP status errors
        log_service.service_error(
            service_name=service_name,
            function_name=function_name,
            status_code=http_err.response.status_code,
            http_status_error={http_err},
        )
        raise HTTPException(status_code=503, detail=message_503)
    except httpx.RequestError as req_err:
        # Log and raise request errors
        log_service.service_error(
            service_name=service_name,
            function_name=function_name,
            status_code=None,
            request_error={req_err},
        )
        raise HTTPException(status_code=503, detail=message_503)
    except ValueError as val_err:
        # Log and raise value errors
        log_service.service_error(
            service_name=service_name,
            function_name=function_name,
            tatus_code=None,
            value_error={val_err},
        )
        raise HTTPException(status_code=503, detail=message_503)
