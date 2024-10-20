from datetime import datetime, timezone

datetime_format: str = "%Y-%m-%dT%H:%M:%S.%f"


class DateTimeUtil:

    @staticmethod
    def get_datetime_now() -> datetime:
        return datetime.now(timezone.utc)

    @staticmethod
    def get_datetime_now_str() -> str:
        return datetime.now(timezone.utc).strftime(datetime_format)[:-3]

    @staticmethod
    def get_datetime_str(datetime: datetime) -> str:
        return datetime.strftime(datetime_format)[:-3]
