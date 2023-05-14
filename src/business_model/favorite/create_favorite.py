from src.core.business_model import BusinessModel, ModelType
from src.data_model.favorite import Favorite


class CreateFavorite(BusinessModel):
    def __init__(self, customer_id, book_id):
        self.customer_id = customer_id
        self.book_id = book_id

        super().__init__(
            model_type=ModelType.insert,
            model=Favorite()
        )

    def run(self, **kwargs):
        favorite = self.model.insert(
            data={
                "cu_id": str(self.customer_id),
                "b_id": str(self.book_id),
            }
        ).get(
            condition={
                "cu_id": {
                    "$value": str(self.customer_id)
                }
            }
        ).show().result

        return favorite

