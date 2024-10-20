from pydantic import BaseModel
from typing import Dict, List, Optional, Any
from datetime import datetime


class ErrorDetail(BaseModel):
    client_application_name: str
    client_application_version: str
    client_application_mode: int
    datetime: datetime
    exception_type: str
    error_message: str
    file_name: Optional[str] = None
    function_name: Optional[str] = None
    line_number: Optional[int] = None
    endpoint: Optional[str] = None
    status_code: Optional[int] = None
    validation_errors: Optional[List[Dict[str, Any]]] = None
