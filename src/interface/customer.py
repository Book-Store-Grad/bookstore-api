from pydantic import BaseModel


class ICustomer(BaseModel):
    name: str
    email: str
    password: str
    gender: bool
