from src.business_model.cart.get_cart_items import GetCartItems
from src.business_model.cart.has_cart_items import HasCartItems
from src.core.business_model import BusinessModel, ModelType
from src.data_model.cart import CartItem
from src.data_model.order import Order
from src.interface.order import IOrder


class GetOrderItems(BusinessModel):
    def __init__(self, order_id: int):
        super().__init__(
            model=CartItem(),
            model_type=ModelType.read
        )
        self.order_id = order_id

    def run(self, data: dict = None, conditions: dict = None) -> list:

        items = self.model.get(
            fields=[
                "{}.*".format(self.model.table_name),
                "cu_customer.cu_name",
                "cu_customer.cu_email",
                "cu_customer.cu_gender"
            ],
            joins={
                "$schema_name": "public",
                "cu_customer": {
                    "$table": "$this",
                    "$type": "innerJoin",  # innerJoin, leftJoin, rightJoin
                    "$on": {
                        "$type": "$eq",
                        "$tableA": "{}.cu_id".format(self.model.table_name),
                        "$tableB": "cu_customer.cu_id",
                    }
                }
            },
            order_by={
                "o_id": "DESC"
            },
        ).show().result

        return items
