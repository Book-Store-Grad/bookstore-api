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
        if self.customer.gender.lower() in ["f", "female"]:
            gender = False
        elif self.customer.gender.lower() in ["m", "male"]:
            gender = True
        else:
            raise Exception("Gender not correctly specified, only M or F is accepted")

        customer = super().run(
            data={
                "cu_name": self.customer.name,
                "cu_email": self.customer.email,
                "cu_password": self.customer.password,
                "cu_gender": str(gender),
                "cu_role": str(self.customer.role),
            }
        ).result

        customer.pop("cu_password", None)
        customer.pop("cu_pw_code", None)

        return customer
