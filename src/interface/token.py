from typing import Optional

from pydantic import BaseModel


class IToken(BaseModel):
    token: str
    customer_id: int
    role: Optional[str]
