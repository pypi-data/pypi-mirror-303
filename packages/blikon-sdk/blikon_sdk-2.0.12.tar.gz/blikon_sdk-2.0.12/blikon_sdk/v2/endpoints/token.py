from fastapi import APIRouter, HTTPException
from blikon_sdk.v2.schemas.shared_schemas import (
    TokenRequest,
    TokenResponse,
    ErrorResponse,
)
from blikon_sdk.v2.core.core import Core
from blikon_sdk.v2.helpers.msg_helper import msg

router = APIRouter()


@router.post(
    "/token",
    tags=["token"],
    description="This endpoint generates an authentication token for API use",
    summary="Generate an authentication token",
    response_model=TokenResponse,
    responses={422: {"model": ErrorResponse}},
)
async def login_for_access_token(credentials: TokenRequest):
    security_service = Core.get_security_service()
    user_authenticated = security_service.authenticate_user(
        credentials.username, credentials.password
    )
    if not user_authenticated:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token_jwt = security_service.create_timed_access_token(
        data={"sub": credentials.username}
    )
    # token_jwt = security_service.create_timed_access_token(data={"sub": credentials.username}, days=365)
    api_response = TokenResponse(
        result=True,
        message=msg("Successfully generated token"),
        token=token_jwt,
        token_type="bearer",
    )
    return api_response
