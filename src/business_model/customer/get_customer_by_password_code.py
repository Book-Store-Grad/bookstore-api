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
            fields=[
                "cu_id as u_id",
                "cu_name as u_name",
                "cu_email as u_email",
                "cu_role as u_role",
                "cu_created_on as u_created_on",
            ],
            condition={
                "cu_pw_code": {
                    "$value": str(self.code)
                }
            }
        ).show(True).result
