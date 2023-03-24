from src.core.business_model import BusinessModel, ModelType
from src.data_model.customer import Customer
from src.interface.customer import ICustomer


class GetCustomerByEmail(BusinessModel):
    def __init__(self, email: str):
        super().__init__(
            model=Customer(),
            model_type=ModelType.read
        )

        self.email = email

    def run(self, data: dict = None, conditions: dict = None) -> dict:
        return self.model.get_one(
            fields=[
                "cu_id",
                "cu_name",
                "cu_email",
                "cu_gender",
                "cu_role",
                "cu_created_on",
                "cu_password",
            ],
            condition={
                "cu_email": {
                    "$value": str(self.email)
                }
            }
        ).show(True).result
