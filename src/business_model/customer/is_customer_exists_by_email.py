from src.business_model.customer.get_customer_by_email import GetCustomerByEmail
from src.core.business_model import BusinessModel, ModelType
from src.data_model.customer import Customer
from src.interface.customer import ICustomer


class IsCustomerExistsByEmail(BusinessModel):
    def __init__(self, email: str):
        super().__init__(
            model=Customer(),
            model_type=ModelType.read
        )

        self.email = email

    def run(self, data: dict = None, conditions: dict = None) -> dict:
        customer = GetCustomerByEmail(
            email=self.email
        ).run()

        return len(customer) > 0
