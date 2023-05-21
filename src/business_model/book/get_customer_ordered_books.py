from src.core.business_model import BusinessModel, ModelType
from src.data_model.book import Book


class GetCustomerOrderedBooks(BusinessModel):
    def __init__(self, customer_id: int = None,):
        self.customer_id = customer_id

        print("customer_id", self.customer_id)

        self.model = Book()

        super().__init__(
            model=self.model,
            model_type=ModelType.read
        )

    def run(self, data: dict = None, conditions: dict = None) -> list:
        books = self.model.add_transaction("""
            select
                *
            from b_book
            where b_id in (
                select b_id from ca_cart_items where cu_id = {customer_id}
            );
        """.format(customer_id=self.customer_id)).show().result

        for book in books:
            book['cover_image_url'] = '/book/{}/image'.format(book['b_id'])

            try:
                book['b_price'] = float(book['b_price'])
            except:
                pass

        return books
