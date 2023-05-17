from src.core.business_model import BusinessModel, ModelType
from src.data_model.author import Author
from view.author import IEditAuthor, IAuthor


class UpdateAuthor(BusinessModel):
    def __init__(self, author_id: int, author: IEditAuthor):
        self.model = Author()

        super().__init__(
            model=self.model,
            model_type=ModelType.update
        )

        self.author_id = author_id
        self.data = author

    def run(self, data: dict = None, conditions: dict = None) -> dict:
        # TODO: Check what fields that the user is updating

        author = super().run(
            data={
                "a_name": self.data.name,
            },
            conditions={
                "a_id": {
                    "$value": str(self.author_id)
                }
            }
        ).result

        print("Author:", author)
        if not author:
            raise Exception("Author not found")

        author = IAuthor(
            id=author['a_id'],
            name=author['a_name'],
        )

        return author
