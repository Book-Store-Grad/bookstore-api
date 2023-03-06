from src.core.business_model import BusinessModel, ModelType
from src.data_model.cart import CartItem


class RemoveFromCart(BusinessModel):
    def __init__(self, cart_item_id: int, customer_id: int):
        super().__init__(
            model=CartItem(),
            model_type=ModelType.delete
        )

        self.cart_item_id = cart_item_id
        self.customer_id = customer_id

    def run(self, data: dict = None, conditions: dict = None) -> dict:
        return super().run(
            conditions={
                "cu_id": self.customer_id,
                "b_id": self.cart_item_id,
            }
        ).result
