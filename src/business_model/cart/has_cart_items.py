from src.core.business_model import BusinessModel, ModelType
from src.data_model.cart import CartItem


class HasCartItems(BusinessModel):
    def __init__(self, customer_id: int):
        super().__init__(
            model=CartItem(),
            model_type=ModelType.read,
        )

        self.customer_id = customer_id

    def run(self, data: dict = None, conditions: dict = None) -> bool:
        items = self.model.get(
            fields=[
                "count(cai_id)"
            ],
            condition={
                "cu_customer.cu_id": {
                    "$value": str(self.customer_id)
                }
            }
        ).show()

        return items.result['count'] > 0
