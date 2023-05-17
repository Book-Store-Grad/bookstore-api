from src.core.business_model import BusinessModel, ModelType
from src.data_model.favorite import Favorite


class DeleteFavorite(BusinessModel):
    def __init__(self, favorite_id):
        self.favorite_id = favorite_id

        super().__init__(
            model_type=ModelType.delete,
            model=Favorite()
        )

    def run(self, data: dict = None, condition: dict = None):
        favorite = self.model.delete(
            conditions={
                "fa_id": {
                    "$value": str(self.favorite_id)
                }
            },
            data={}
        )
        return favorite.commit().result
