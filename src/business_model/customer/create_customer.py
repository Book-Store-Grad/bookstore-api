from src.core.business_model import BusinessModel, ModelType
from src.data_model.customer import Customer
from src.interface.customer import ICustomer


class CreateCustomer(BusinessModel):
    def __init__(self, customer: ICustomer):
        super().__init__(
            model=Customer(),
            model_type=ModelType.insert
        )

        self.customer = customer

    def run(self, data: dict = None, conditions: dict = None) -> dict:
        customer = super().run(
            data={
                "cu_name": self.customer.name,
                "cu_email": self.customer.email,
                "cu_password": self.customer.password,
                "cu_gender": str(False) if self.customer.gender == "F" else str(True),
            }
        ).result

        customer.pop("cu_password", None)
        customer.pop("cu_pw_code", None)

        return customer
