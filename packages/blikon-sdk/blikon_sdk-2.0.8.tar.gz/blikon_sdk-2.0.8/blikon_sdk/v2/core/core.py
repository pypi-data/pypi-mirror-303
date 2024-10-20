import httpx
from fastapi import FastAPI
from blikon_sdk.v2.models.sdk_configuration_model import SDKConfiguration
from blikon_sdk.v2.services.log_service import LogService
from blikon_sdk.v2.services.security_service import SecurityService


class Core:

    _app: FastAPI = None
    _app_configuration = None  # Type is open to customize
    _sdk_configuration: SDKConfiguration = None
    _httpx_client: httpx.AsyncClient = None
    _log_service: LogService = None
    _security_service: SecurityService = None

    @classmethod
    def set_app(cls, app: FastAPI):
        cls._app = app

    @classmethod
    def get_app(cls) -> FastAPI:
        if cls._app is None:
            raise RuntimeError("App instance is not set")
        return cls._app

    @classmethod
    def set_sdk_configuration(cls, sdk_configuration: SDKConfiguration):
        cls._sdk_configuration = sdk_configuration

    @classmethod
    def get_sdk_configuration(cls) -> SDKConfiguration:
        if cls._sdk_configuration is None:
            raise RuntimeError("SDK Configuration instance is not set")
        return cls._sdk_configuration

    @classmethod
    def set_app_configuration(cls, app_configuration):
        cls._app_configuration = app_configuration

    @classmethod
    def get_app_configuration(cls):
        if cls._app_configuration is None:
            raise RuntimeError("App Configuration instance is not set")
        return cls._app_configuration

    @classmethod
    def set_httpx_client(cls, httpx_client: httpx.AsyncClient):
        cls._httpx_client = httpx_client

    @classmethod
    def get_httpx_client(cls):
        if cls._httpx_client is None:
            raise RuntimeError("Httpx Client instance is not set")
        return cls._httpx_client

    @classmethod
    def set_log_service(cls, log_service: LogService):
        cls._log_service = log_service

    @classmethod
    def get_log_service(cls) -> LogService:
        if cls._log_service is None:
            raise RuntimeError("Log Service instance is not set")
        return cls._log_service

    @classmethod
    def set_security_service(cls, security_service: SecurityService):
        cls._security_service = security_service

    @classmethod
    def get_security_service(cls) -> SecurityService:
        if cls._security_service is None:
            raise RuntimeError("Security Service instance is not set")
        return cls._security_service
