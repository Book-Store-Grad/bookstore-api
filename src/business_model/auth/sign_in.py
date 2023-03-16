from src.business_model.customer.get_customer_by_email import GetCustomerByEmail
from src.core.business_model import BusinessModel, ModelType
from src.data_model.customer import Customer


class SignIn(BusinessModel):
    def __init__(self, email: str, password: str):
        super().__init__(
            model=Customer(),
            model_type=ModelType.read,
        )

        self.email = email
        self.password = password

    def run(self, data: dict = None, conditions: dict = None) -> dict:
        customer = GetCustomerByEmail(
            email=self.email,
        ).run()

        if customer['cu_gender'] is True:
            customer['cu_gender'] = "male"
        else:
            customer['cu_gender'] = "female"

        if customer is None:
            return None

        if customer["cu_password"] != self.password:
            return None

        customer.pop("cu_password", None)

        return customer
