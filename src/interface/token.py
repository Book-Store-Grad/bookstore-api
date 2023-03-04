from pydantic import BaseModel


class IToken(BaseModel):
    token: str
    cu_id: int
