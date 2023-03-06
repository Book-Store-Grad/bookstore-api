from src.business_model.cart.get_cart_items import GetCartItems
from src.business_model.cart.has_cart_items import HasCartItems
from src.business_model.order.get_order_items import GetOrderItems
from src.core.business_model import BusinessModel, ModelType
from src.data_model.order import Order
from src.interface.order import IOrder


class GetOrder(BusinessModel):
    def __init__(self, order_id: int):
        super().__init__(
            model=Order(),
            model_type=ModelType.insert
        )
        self.order_id = order_id

    def run(self, data: dict = None, conditions: dict = None) -> bool:

        order = self.model.get_one(
            condition={
                "o_id": {
                    "$value": str(self.order_id)
                }
            }
        ).get_one(
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
        ).show(True).result

        order['order_items'] = GetOrderItems(
            order_id=order['o_id']
        ).run()

        return order
