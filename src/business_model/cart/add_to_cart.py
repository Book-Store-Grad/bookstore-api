from src.core.business_model import BusinessModel, ModelType
from src.data_model.cart import CartItem


class AddToCart(BusinessModel):
    def __init__(self, book_id: int, customer_id: int):
        super().__init__(
            model=CartItem(),
            model_type=ModelType.insert
        )

        self.book_id = book_id
        self.customer_id = customer_id

    def run(self, data: dict = None, conditions: dict = None) -> dict:
        return super().run(
            data={
                "cu_id": str(self.customer_id),
                "b_id": str(self.book_id),
            }
        ).result
