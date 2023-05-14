from src.core.business_model import BusinessModel, ModelType
from src.data_model.favorite import Favorite


class GetFavorite(BusinessModel):
    def __init__(self, favorite_id):
        self.favorite_id = favorite_id

        super().__init__(
            model_type=ModelType.read,
            model=Favorite()
        )

    def run(self):
        favorite = self.model.get_one(
            condition={
                "fa_id": {
                    "value": str(self.favorite_id)
                }
            }
        )

        return favorite.show(True).result

