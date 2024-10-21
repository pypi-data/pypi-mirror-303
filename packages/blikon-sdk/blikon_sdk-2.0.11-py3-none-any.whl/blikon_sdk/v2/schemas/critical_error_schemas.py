from pydantic import BaseModel
from typing import Optional


class CriticalError(BaseModel):
    client_application_id: str
    exception_type: str
    error_message: str
    criticality: int
    traceback: Optional[str]
    file_name: Optional[str]
    function_name: Optional[str]
    line_number: Optional[int]
    endpoint: Optional[str]
    method: Optional[str]
    status_code: Optional[int]
    additional_info: Optional[dict]
