from pydantic import BaseModel


class ICreateOrder(BaseModel):
    customer_id: int


class IOrder(BaseModel):
    customer_id: int

