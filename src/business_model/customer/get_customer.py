from src.core.business_model import BusinessModel, ModelType
from src.data_model.customer import Customer
from src.interface.customer import ICustomer


class GetCustomer(BusinessModel):
    def __init__(self, customer_id: int):
        super().__init__(
            model=Customer(),
            model_type=ModelType.read
        )

        self.customer_id = customer_id

    def run(self, data: dict = None, conditions: dict = None) -> dict:
        customer = self.model.get_one(
            fields=[
                "cu_id",
                "cu_name",
                "cu_email",
                "cu_gender",
                "cu_role",
                "cu_created_on",
            ],
            condition={
                "cu_id": {
                    "$value": str(self.customer_id)
                }
            }
        ).show(True).result

        customer['cu_gender'] = "male" if str(customer['cu_gender']).lower() == "true" else "female"

        return customer
