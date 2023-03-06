from src.business_model.cart.get_cart_items import GetCartItems
from src.business_model.cart.has_cart_items import HasCartItems
from src.business_model.order.get_order_items import GetOrderItems
from src.core.business_model import BusinessModel, ModelType
from src.data_model.order import Order
from src.interface.order import IOrder


class GetOrders(BusinessModel):
    def __init__(self, customer_id: int):
        super().__init__(
            model=Order(),
            model_type=ModelType.insert
        )

        self.customer_id = customer_id

    def run(self, data: dict = None, conditions: dict = None) -> bool:

        order = self.model.get(
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
            condition={
                "cu_customer.cu_id": {
                    "$value": str(self.customer_id)
                }
            },
            order_by={
                "o_id": "DESC"
            },
        ).show().result

        return order
