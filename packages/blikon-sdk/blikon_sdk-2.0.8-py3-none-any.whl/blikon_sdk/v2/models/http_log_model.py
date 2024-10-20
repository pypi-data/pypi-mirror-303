from pydantic import BaseModel


class HttpLog(BaseModel):
    endpoint: str
    method: str
    start_time: str
    client_ip: str
    user_agent: str
    operating_system: str
    browser: str
    request_params: str
    request_body: str
    end_time: str
    duration: str
    status_code: str
    response_body: str
