from src.core.business_model import BusinessModel, ModelType
from src.data_model.favorite import Favorite


class UpdateFavorites(BusinessModel):
    def __init__(self, favorite_id: int,):
        self.favorite_id = favorite_id

        super().__init__(
            model=Favorite(),
            model_type=ModelType.update,
        )

    def run(self, condition: dict = None, data: dict = None):
        return 'update_favorite'
