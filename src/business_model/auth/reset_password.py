from random import random

from src.core.business_model import BusinessModel, ModelType
from src.data_model.customer import Customer


class ResetPassword(BusinessModel):
    def __init__(self, customer_id: int, code: str, password: str):
        super().__init__(
            model=Customer(),
            model_type=ModelType.update
        )

        self.customer_id = customer_id
        self.password = password
        self.code = code

    def run(self, data: dict = None, conditions: dict = None):

        customer = self.model.get_one(
            condition={
                "cu_id": {
                    "$value": int(self.customer_id)
                }
            },

        ).show(True).result

        if customer is None:
            return False

        if customer["cu_pw_code"] != self.code:
            return False

        self.model.update(
            conditions={
                "cu_id": {
                    "$value": str(self.customer_id)
                }
            },
            data={
                "cu_password": str(self.password)
            }
        ).commit()

        return True
