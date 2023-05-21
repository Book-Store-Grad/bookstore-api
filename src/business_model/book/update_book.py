from src.core.business_model import BusinessModel, ModelType
from src.data_model.book import Book
from view.book import IEditBook, IBook


class UpdateBook(BusinessModel):
    def __init__(self, book_id: int, book: IEditBook):
        self.model = Book()

        super().__init__(
            model=self.model,
            model_type=ModelType.update
        )

        self.book_id = book_id
        self.data = book

    def run(self, data: dict = None, conditions: dict = None) -> dict:
        # TODO: Check what fields that the user is updating

        try:
            self.data.price = float(self.data.price)
        except:
            raise Exception("Invalid price")

        book = super().run(
            data={
                "b_name": self.data.name,
                "b_genre": self.data.genre,
                "b_price": self.data.price,
                "b_description": self.data.description,
                "a_id": self.data.author_id,
            },
            conditions={
                "b_id": {
                    "$value": str(self.book_id)
                }
            }
        ).result

        book = IBook(
            id=book['b_id'],
            name=book['b_name'],
            price=float(book['b_price']),
            genre=book['b_genre'],
            description=book['b_description'],
        )

        return book
