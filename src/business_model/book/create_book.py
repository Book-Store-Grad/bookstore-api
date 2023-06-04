from src.core.business_model import BusinessModel, ModelType
from src.data_model.book import Book
from view.book import IBook, IEditBook


class CreateBook(BusinessModel):
    def __init__(self, book: IEditBook, author_id: int):
        self.model = Book()
        self.book = book
        self.author_id = author_id

        super().__init__(
            model=self.model,
            model_type=ModelType.insert
        )

    def run(self, data: dict = None, conditions: dict = None) -> dict:
        create = super().run(
            data={
                "b_name": self.book.name,
                "b_price": str(self.book.price),
                "b_genre": self.book.genre,
                "b_description": self.book.description,
                "a_id": str(self.author_id),
            }
        ).result

        return create
