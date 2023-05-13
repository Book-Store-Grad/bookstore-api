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
        sql = """
            select 
                CASE WHEN b_price = '0' THEN True ELSE CASE WHEN b_price = '' THEN True ELSE FALSE END END as is_free,
                b_id in (select b_id from ca_cart_items where cu_id = 25) as is_owned,
                *
            from b_book
            where b_id = '{}';
        """.format(self.book_id)

        book = self.model.add_transaction(sql).show(True).result

        book['cover_image_url'] = '/book/{}/image'.format(self.book_id)

        return book
