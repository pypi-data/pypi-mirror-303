import re
from fastapi.exceptions import RequestValidationError
from blikon_sdk.v2.helpers.msg_helper import msg


def raise_error(field: str, message: str) -> None:
    errors = [
        {
            "loc": ("body", field),
            "msg": msg(message),
            "type": "value_error",
        }
    ]
    raise RequestValidationError(errors)


def validate_id(value: int, field: str, required: bool) -> int:
    if required and value is None:
        raise_error(field, "The field is required")

    if value is not None and value <= 0:
        raise_error(field, "Must be an integer greater than zero")

    return value


def validate_uuid(value: str, field: str, required: bool) -> str:
    if required and not value:
        raise_error(field, "The field is required")

    uuid_pattern = re.compile(
        r"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$"
    )
    if value and not uuid_pattern.match(value):
        raise_error(field, "Must be in a valid UUID format")

    return value


def validate_email(value: str, field: str, required: bool) -> str:
    if required and not value:
        raise_error(field, "The field is required")

    email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    if value and not email_pattern.match(value):
        raise_error(field, "Must be in a valid email format")

    return value


def validate_phone_number(value: str, field: str, required: bool) -> str:
    if required and not value:
        raise_error(field, "The field is required")

    phone_pattern = re.compile(r"^\d{12}$")
    if value and not phone_pattern.match(value):
        raise_error(field, "Must have exactly 12 digits")

    return value


def validate_string(value: str, field: str, required: bool, max_length: int) -> str:
    if required and not value:
        raise_error(field, "The field is required")

    # Adjust the interpolation of the max_length value
    string_pattern = re.compile(rf"^[\w\W\s\S]{{0,{max_length}}}$")

    if value and not string_pattern.match(value):
        raise_error(
            field,
            f"Must be in a valid string format, with a maximum of {max_length} characters",
        )

    return value


def validate_token(value: str, field: str, required: bool) -> str:
    if required and not value:
        raise_error(field, "The field is required")

    pattern = re.compile(r"^[A-Za-z0-9-_]+(?:\.[A-Za-z0-9-_]+){2}$")

    if value and not pattern.match(value):
        raise_error(
            field,
            f"Must be in a valid JWT format",
        )

    return value
