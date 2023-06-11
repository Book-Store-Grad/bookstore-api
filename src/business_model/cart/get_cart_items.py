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
        books = self.model.get(
            joins={
                "$schema_name": "public",
                "cu_customer": {
                    "$table": "$this",
                    "$type": "innerJoin",  # innerJoin, leftJoin, rightJoin
                    "$on": {
                        "$type": "$eq",
                        "$tableA": "{}.cu_id".format(self.model.table_name),
                        "$tableB": "cu_customer.cu_id",
                    }
                },
                "b_book": {
                    "$table": "$this",
                    "$type": "innerJoin",  # innerJoin, leftJoin, rightJoin
                    "$on": {
                        "$type": "$eq",
                        "$tableA": "{}.b_id".format(self.model.table_name),
                        "$tableB": "b_book.b_id",
                    }
                }
            },
            condition={
                "cu_customer.cu_id": {
                    "$value": str(self.customer_id)
                }
            }
        ).show().result

        print("books:", books)

        items = []
        for book in books:
            items.append({
                "cover_image_url": "/book/{}/image".format(book["b_id"]),
                "cai_id": book["cai_id"],
                "b_id": book["b_id"],
                "b_name": book["b_name"],
                "b_price": book["b_price"],
                "b_genre": book["b_genre"],
                "b_description": book["b_description"],
            })


        return items