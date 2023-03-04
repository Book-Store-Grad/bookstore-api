from typing import Any

from src.core.business_model import BusinessModel, ModelType
from src.data_model.book import Book


class DeleteBook(BusinessModel):
    def __init__(self, book_id: int):
        self.model = Book()

        super().__init__(
            model=self.model,
            model_type=ModelType.read
        )

        self.book_id = book_id

    def run(self, data: dict = None, conditions: dict = None) -> Any:
        return self.model.delete(
            data={},
            conditions={
                "b_id": self.book_id
            }
        ).commit().result
