from src.core.business_model import BusinessModel, ModelType
from src.data_model.cart import CartItem


class GetCartItems(BusinessModel):
    def __init__(self, customer_id: int):
        super().__init__(
            model=CartItem(),
            model_type=ModelType.read,
        )

        self.customer_id = customer_id

    def run(self, data: dict = None, conditions: dict = None) -> list:
        return self.model.get(
            condition={
                "cu_id": {
                    "$value": str(self.customer_id)
                }
            }
        ).show().result
