from src.core.business_model import BusinessModel, ModelType
from src.data_model.book import Book
from view.book import IBook, IEditBook


class CreateBook(BusinessModel):
    def __init__(self, book: IEditBook):
        self.model = Book()
        self.book = book

        super().__init__(
            model=self.model,
            model_type=ModelType.insert
        )

    def run(self, data: dict = None, conditions: dict = None) -> dict:
        create = super().run(
            data={
                "b_name": self.book.name,
                "b_price": self.book.price,
                "b_genre": self.book.genre,
                "b_description": self.book.description,
            }
        ).result

        return create
