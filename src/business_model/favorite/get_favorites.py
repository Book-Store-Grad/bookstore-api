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
            },
            joins={
                "$schema_name": "public",
                "b_book": {
                    "$table": "$this",
                    "$type": "innerJoin",  # innerJoin, leftJoin, rightJoin
                    "$on": {
                        "$type": "$eq",
                        "$tableA": "{}.b_id".format(self.model.table_name),
                        "$tableB": "b_book.b_id",
                    }
                },
            },
        ).show().result

        for favorite in favorites:
            favorite['cover_image_url'] = '/book/{}/image'.format(favorite['b_id'])

            try:
                favorite['b_price'] = float(favorite['b_price'])
            except:
                pass

        return favorites

