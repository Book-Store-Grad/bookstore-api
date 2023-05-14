from src.core.business_model import BusinessModel, ModelType
from src.data_model.favorite import Favorite


class GetFavorites(BusinessModel):
    def __init__(self, customer_id):
        self.customer_id = customer_id

        super().__init__(
            model_type=ModelType.read,
            model=Favorite()
        )

    def run(self, conditions: dict = None, data: dict = None):
        favorites = self.model.get(
            condition={
                "cu_id": {
                    "$value": str(self.customer_id)
                }
            }
        ).show().result
        return favorites

