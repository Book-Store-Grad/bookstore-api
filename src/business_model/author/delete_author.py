from typing import Any

from src.core.business_model import BusinessModel, ModelType
from src.data_model.author import Author


class DeleteAuthor(BusinessModel):
    def __init__(self, author_id: int):
        self.model = Author()

        super().__init__(
            model=self.model,
            model_type=ModelType.read
        )

        self.author_id = author_id

    def run(self, data: dict = None, conditions: dict = None) -> Any:
        return self.model.delete(
            data={},
            conditions={
                "a_id": {
                    "$value": str(self.author_id)
                }
            }
        ).commit().result
