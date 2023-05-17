from src.core.business_model import BusinessModel, ModelType
from src.data_model.author import Author


class GetAuthors(BusinessModel):
    def __init__(self, query: str = None):
        self.query = query

        self.model = Author()

        super().__init__(
            model=self.model,
            model_type=ModelType.read
        )

    def run(self, data: dict = None, conditions: dict = None) -> list:
        # Add field is_favorite
        # Add is_owned
        # Add is_free

        conditions = []

        has_condition = ""
        if self.query:
            has_condition = "where "
            if self.query:
                conditions.append(f"b_name LIKE '{self.query}%'")

        conditions = "AND ".join(conditions)

        print("conditions", conditions)

        sql = """
            select
                *
            from a_author 
            {has_condition} {conditions};
        """.format(has_condition=has_condition, conditions=conditions)

        return self.model.add_transaction(sql).show().result
