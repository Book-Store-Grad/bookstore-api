from random import random

from src.core.business_model import BusinessModel, ModelType
from src.data_model.customer import Customer


class UpdateForgetPasswordCode(BusinessModel):
    def __init__(self, customer_id: int):
        super().__init__(
            model=Customer(),
            model_type=ModelType.update
        )

        self.customer_id = customer_id

    def run(self, data: dict = None, conditions: dict = None):
        code = int(random() * 10000)

        self.model.update(
            conditions={
                "cu_id": {
                    "$value": int(self.customer_id)
                }
            },
            data={
                "cu_pw_code": str(code)
            }
        ).commit()

        return code
