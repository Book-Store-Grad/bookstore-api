from typing import Union

from databaser.engine.result import ExecutionResult

from src.core.business_model import BusinessModel, ModelType
from src.data_model.customer import Customer


class UpdateResetField(BusinessModel):
    def __init__(self, value: bool, customer_id: int):
        super().__init__(
            Customer(),
            ModelType.update
        )

        self.value = value
        self.customer_id = customer_id

    def run(self, data: dict = None, conditions: dict = None) -> bool:

        self.model.update(
            conditions={
                "cu_id": {
                    "$value": str(self.customer_id)
                }
            },
            data={
                "reset_password": str(self.value)
            }
        )

        return True
