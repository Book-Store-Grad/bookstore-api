from src.business_model.favorite.get_favorites import GetFavorites
from src.core.business_model import BusinessModel, ModelType
from src.data_model.book import Book


# TODO: Add is_favorite
class GetBook(BusinessModel):
    def __init__(self, book_id: int, customer_id: int = None):
        self.model = Book()

        super().__init__(
            model=self.model,
            model_type=ModelType.read
        )

        self.book_id = book_id

        self.customer_id = customer_id

    def run(self, data: dict = None, conditions: dict = None) -> dict:
        sql = """
            select 
                CASE WHEN b_price = '0' THEN True ELSE CASE WHEN b_price = '' THEN True ELSE FALSE END END as is_free,
                b_id in (select b_id from ca_cart_items where cu_id = 25) as is_owned,
                *
            from b_book
            where b_id = '{}';
        """.format(self.book_id)

        book = self.model.add_transaction(sql).show(True).result

        if not book:
            return None

        book['is_favorite'] = False

        print("Book:", book)

        if self.customer_id:
            favorites = GetFavorites(
                customer_id=self.customer_id
            ).run()

            favorites_book_ids = [favorite['b_id'] for favorite in favorites]

            book['is_favorite'] = book['b_id'] in favorites_book_ids

        book['cover_image_url'] = '/book/{}/image'.format(self.book_id)

        try:
            book['b_price'] = float(book['b_price'])
        except ValueError:
            book['b_price'] = 0

        return book
