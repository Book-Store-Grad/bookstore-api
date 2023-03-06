from src.business_model.cart.get_cart_items import GetCartItems
from src.business_model.cart.has_cart_items import HasCartItems
from src.core.business_model import BusinessModel, ModelType
from src.data_model.order import Order
from src.interface.order import IOrder


class CreateOrder(BusinessModel):
    def __init__(self, order: IOrder):
        super().__init__(
            model=Order(),
            model_type=ModelType.insert
        )
        self.order = order

    def run(self, data: dict = None, conditions: dict = None) -> bool:

        has_items = HasCartItems(
            self.order.customer_id
        ).run()
        print("Has Items:", has_items)

        if not has_items:
            return False

        items = GetCartItems(
            customer_id=self.order.customer_id,
        ).run()

        print("Items:", items[0])

        total = 0
        for item in items:
            total += int(item['b_price'])

        order = self.model.insert(
            data={
                "cu_id": str(self.order.customer_id),
                "o_total": str(total)
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

        order['order_items'] = items

        return order
