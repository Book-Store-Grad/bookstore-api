from pydantic import BaseModel


class Response(BaseModel):
    access_token: str
    status_code: int
    message: str
    content: dict
