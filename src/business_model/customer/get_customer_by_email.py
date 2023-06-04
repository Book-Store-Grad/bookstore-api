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
        customer = self.model.get_one(
            fields=[
                "cu_id as u_id",
                "cu_name as u_name",
                "cu_email as u_email",
                "cu_gender as u_gender",
                "cu_role as u_role",
                "cu_created_on as u_created_on",
                "cu_password",
            ],
            condition={
                "cu_email": {
                    "$value": str(self.email)
                }
            }
        ).show(True).result

        gender = 'male'
        print("customer", customer)
        if len(customer) == 0:
            return {}

        if not customer['u_gender']:
            gender = 'female'

        customer['u_gender'] = gender

        return customer
