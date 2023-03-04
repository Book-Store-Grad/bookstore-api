from pydantic import BaseModel


class ICreateOrder(BaseModel):
    customer_id: int


class IOrder(BaseModel):
    cu_id: int


class IGetOrders(BaseModel):
    customer_id: int
