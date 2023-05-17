from src.core.business_model import BusinessModel, ModelType
from src.data_model.author import Author


class GetAuthor(BusinessModel):
    def __init__(self, author_id: int):
        self.model = Author()

        super().__init__(
            model=self.model,
            model_type=ModelType.read
        )

        self.author_id = author_id

    def run(self, data: dict = None, conditions: dict = None) -> dict:
        sql = """
            select 
                *
            from a_author
            where a_id = '{}';
        """.format(self.author_id)

        author = self.model.add_transaction(sql).show(True).result

        return author
