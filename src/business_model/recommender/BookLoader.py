import pandas as pd

from src.business_model.book.get_books import GetBooks


class BookLoader:
    def get_books(self) -> pd.DataFrame:
        books = self.load_books()

        # Sample book dataset
        books = pd.DataFrame(books)
        books.to_csv('books.csv', index=False)

        return books

    def load_books(self):
        return GetBooks().run()
