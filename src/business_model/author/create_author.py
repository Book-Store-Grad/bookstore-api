from src.core.business_model import BusinessModel, ModelType
from src.data_model.author import Author
from view.author import IEditAuthor


class CreateAuthor(BusinessModel):
    def __init__(self, author: IEditAuthor):
        self.model = Author()
        self.author = author

        super().__init__(
            model=self.model,
            model_type=ModelType.insert
        )

    def run(self, data: dict = None, conditions: dict = None) -> dict:
        create = super().run(
            data={
                "a_name": self.author.name,
            }
        ).result

        return create
