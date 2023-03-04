from src.core.business_model import BusinessModel, ModelType
from src.data_model.book import Book


class GetBooks(BusinessModel):
    def __init__(self):
        self.model = Book()

        super().__init__(
            model=self.model,
            model_type=ModelType.read
        )

    def run(self, data: dict = None, conditions: dict = None) -> list:
        return self.model.get().show().result
