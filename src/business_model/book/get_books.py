from src.core.business_model import BusinessModel, ModelType
from src.data_model.book import Book


class GetBooks(BusinessModel):
    def __init__(self, query: str = None):
        self.query = query

        self.model = Book()

        super().__init__(
            model=self.model,
            model_type=ModelType.read
        )

    def run(self, data: dict = None, conditions: dict = None) -> list:
        # Add field is_favorite
        # Add is_owned
        # Add is_free
        sql = """
            select
                CASE WHEN b_price = '0' THEN True ELSE CASE WHEN b_price = '' THEN True ELSE FALSE END END as is_free,
                b_id in (select b_id from ca_cart_items where cu_id = 25) as is_owned,
                *
            from b_book ;
        """

        if self.query:
            sql = """
                select
                    CASE WHEN b_price = '0' THEN True ELSE CASE WHEN b_price = '' THEN True ELSE FALSE END END as is_free,
                    b_id in (select b_id from ca_cart_items where cu_id = 25) as is_owned,
                    *
                from b_book 
                where b_name LIKE '{}%';
            """.format(self.query)
        return self.model.add_transaction(sql).show().result
