from pydantic import BaseModel, field_validator
from typing import Dict, List, Optional, Any
from blikon_sdk.v2.helpers.msg_helper import msg


class ApiResponse(BaseModel):
    """
    Base API response model
    """

    result: bool
    message: str


class ErrorResponse(ApiResponse):
    """
    Base error API response model
    """

    exception_type: str
    validation_errors: Optional[List[Dict[str, Any]]] = None


class TokenRequest(BaseModel):
    """
    Token request model
    """

    username: str
    password: str

    @field_validator("username")
    def validate_username(cls, value):
        if not value:
            raise ValueError(msg("The field is required"))
        if not (4 <= len(value) <= 21):
            raise ValueError(msg("Username must be 5 to 20 characters"))
        return value

    @field_validator("password")
    def validate_password(cls, value):
        if not value:
            raise ValueError(msg("The field is required"))
        if not (4 <= len(value) <= 21):
            raise ValueError(msg("Password must be 5 to 20 characters"))
        return value


class TokenResponse(ApiResponse):
    """
    Token response model
    """

    token: str
    token_type: str
