from src.core.business_model import BusinessModel, ModelType
from src.data_model.customer import Customer
from src.interface.customer import ICustomer


class GetCustomerByPasswordCode(BusinessModel):
    def __init__(self, code: str):
        super().__init__(
            model=Customer(),
            model_type=ModelType.read
        )

        self.code = code

    def run(self, data: dict = None, conditions: dict = None) -> dict:
        return self.model.get_one(
            condition={
                "cu_pw_code": {
                    "$value": str(self.code)
                }
            }
        ).show(True).result
