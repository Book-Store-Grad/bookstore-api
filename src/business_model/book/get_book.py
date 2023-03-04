from src.core.business_model import BusinessModel, ModelType
from src.data_model.book import Book


class GetBook(BusinessModel):
    def __init__(self, book_id: int):
        self.model = Book()

        super().__init__(
            model=self.model,
            model_type=ModelType.read
        )

        self.book_id = book_id

    def run(self, data: dict = None, conditions: dict = None) -> dict:
        return self.model.get(
            condition={
                "b_id": {
                    "$value": str(self.book_id)
                }
            }
        ).show(True).result
