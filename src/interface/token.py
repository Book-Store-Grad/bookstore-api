from pydantic import BaseModel


class IToken(BaseModel):
    token: str
    customer_id: int
