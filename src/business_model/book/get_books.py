from src.core.business_model import BusinessModel, ModelType
from src.data_model.book import Book


# TODO: Add is_favorite
class GetBooks(BusinessModel):
    def __init__(self, query: str = None, category: str = None, author_id: int = None):
        self.query = query

        self.category = category
        self.author_id = author_id

        print("category", self.category)

        self.model = Book()

        super().__init__(
            model=self.model,
            model_type=ModelType.read
        )

    def get_in_ids(self, ids: list) -> list:
        return self.model.add_transaction(
            """SELECT 
                CASE WHEN b_price = '0' THEN True ELSE CASE WHEN b_price = '' THEN True ELSE FALSE END END as is_free,
                b_id in (select b_id from ca_cart_items where cu_id = 25) as is_owned,
                * 
                FROM b_book WHERE b_id IN ({})""".format(",".join(ids))).show().result

    def run(self, data: dict = None, conditions: dict = None) -> list:
        # Add field is_favorite
        # Add is_owned
        # Add is_free

        if conditions is None:
            conditions = []

        has_condition = ""
        if self.category or self.author_id or self.query:
            has_condition = "where "

            if self.category:
                conditions.append(f"b_genre = '{self.category}'")

            if self.author_id:
                conditions.append(f"a_id = {self.author_id}")

            if self.query:
                conditions.append(f"b_name LIKE '{self.query}%'")

        conditions = "AND ".join(conditions)

        print("conditions", conditions)

        sql = """
            select
                CASE WHEN b_price = '0' THEN True ELSE CASE WHEN b_price = '' THEN True ELSE FALSE END END as is_free,
                b_id in (select b_id from ca_cart_items where cu_id = 25) as is_owned,
                *
            from b_book 
            {has_condition} {conditions};
        """.format(has_condition=has_condition, conditions=conditions)

        books = self.model.add_transaction(sql).show().result

        for book in books:
            book['cover_image_url'] = '/book/{}/image'.format(book['b_id'])

            try:
                book['b_price'] = float(book['b_price'])
            except:
                book['b_price'] = 0.0

        return books
