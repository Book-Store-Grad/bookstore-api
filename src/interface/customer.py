from typing import Optional

from pydantic import BaseModel


class ICustomer(BaseModel):
    name: str
    email: str
    password: str
    gender: str


class IUpdateCustomer(BaseModel):
    name: Optional[str]
    gender: Optional[str]
