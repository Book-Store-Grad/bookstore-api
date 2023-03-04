from src.core.business_model import BusinessModel, ModelType
from src.data_model.cart import CartItem


class GetCartItem(BusinessModel):
    def __init__(self, customer_id: int, cart_item_id: int):
        super().__init__(
            model=CartItem(),
            model_type=ModelType.read,
        )

        self.customer_id = customer_id
        self.cart_item_id = cart_item_id

    def run(self, data: dict = None, conditions: dict = None) -> dict:
        return self.model.get_one(
            condition={
                "cu_id": {
                    "$value": str(self.customer_id)
                },
                "cai_id": {
                    "$value": str(self.cart_item_id)
                },
            }
        ).show(True).result
