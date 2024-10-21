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
        if not (5 <= len(value) <= 50):
            raise ValueError(msg("Must be 5 to 50 characters"))
        if " " in value:
            raise ValueError(msg("Must not contain spaces"))
        return value

    @field_validator("password")
    def validate_password(cls, value):
        if not value:
            raise ValueError(msg("The field is required"))
        if not (5 <= len(value) <= 50):
            raise ValueError(msg("Must be 5 to 50 characters"))
        if " " in value:
            raise ValueError(msg("Must not contain spaces"))
        return value


class TokenResponse(ApiResponse):
    """
    Token response model
    """

    token: str
    token_type: str
