from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from datetime import timedelta
from jose import jwt, JWTError
from typing import Optional, Tuple
from blikon_sdk.v2.models.sdk_configuration_model import SDKConfiguration
from blikon_sdk.v2.utils.utils import DateTimeUtil


class SecurityService:
    def __init__(self, sdk_configuration: SDKConfiguration):
        self.sdk_configuration = sdk_configuration

    def authenticate_user(self, username: str, password: str) -> bool:
        """
        Validates authorization against the provided username and password
        :param username:
        :param password:
        :return:
        """
        if (
            username == self.sdk_configuration.env_settings.API_USER
            and password == self.sdk_configuration.env_settings.API_USER_PASSWORD
        ):
            return True
        else:
            return False

    def create_access_token(self, data: dict) -> str:
        """
        Creates a JWT access token depending on the SDK configuration
        :param data: The payload to be encoded
        :return: The JWT access token
        """
        expiration = DateTimeUtil.get_datetime_now() + (
            timedelta(
                minutes=self.sdk_configuration.env_settings.JWT_EXPIRATION_TIME_MINUTES
            )
        )
        data.update({"exp": expiration})
        payload = data.copy()
        encoded_jwt_token = jwt.encode(
            payload,
            self.sdk_configuration.env_settings.JWT_SECRET,
            algorithm=self.sdk_configuration.sdk_settings.jwt_algorithm,
        )
        return encoded_jwt_token

    def create_timed_access_token(self, data: dict, days: int = 365) -> str:
        """
        Creates a JWT access token depending on the SDK configuration, with custom expiration
        :param data: The payload to be encoded
        :param days: The number of days to expire
        :return: The JWT access token
        """
        expiration = DateTimeUtil.get_datetime_now() + timedelta(days=days)
        data.update({"exp": expiration})
        payload = data.copy()
        encoded_jwt_token = jwt.encode(
            payload,
            self.sdk_configuration.env_settings.JWT_SECRET,
            algorithm=self.sdk_configuration.sdk_settings.jwt_algorithm,
        )
        return encoded_jwt_token

    def decode_token(self, token: str) -> Optional[dict]:
        """
        Decodes a JWT access token
        :param token: The JWT access token
        :return: A decoded payload dictionary
        """
        try:
            decoded_token = jwt.decode(
                token,
                self.sdk_configuration.env_settings.JWT_SECRET,
                algorithms=[self.sdk_configuration.sdk_settings.jwt_algorithm],
                options={"verify_exp": False},
            )
        except JWTError:
            return None
        return decoded_token

    async def verify_token(
        self, token: str
    ) -> Tuple[bool, str, Optional[dict[str, str]]]:
        """
        Verifies a JWT access token
        :param token: The JWT access token
        :return: A tuple of three values, result, message, and the payload decoded from the JWT token as a dictionary
        """
        try:
            decoded_token = jwt.decode(
                token,
                self.sdk_configuration.env_settings.JWT_SECRET,
                algorithms=[self.sdk_configuration.sdk_settings.jwt_algorithm],
                options={"verify_exp": True},
            )
        except JWTError as e:
            if str(e) == "Signature verification failed.":
                return False, "Signature verification failed", None
            elif str(e) == "Signature has expired.":
                return False, "Signature has expired", None
            else:
                return False, "Invalid token", None
        return True, "Token is valid", decoded_token

    async def verify_authorization(
        self, credentials: HTTPAuthorizationCredentials
    ) -> None:
        """
        Verifies a JWT access token
        :param credentials: The 'HTTPAuthorizationCredentials' object
        :return: True if the JWT access token is valid, False otherwise
        """
        token = credentials.credentials
        valid_token, message, payload = await self.verify_token(token)

        if not valid_token:
            message = "Unauthorized"
            raise HTTPException(status_code=401, detail=message)
