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
            raise Exception("Gender not correctly specified, only male or female is accepted")

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

        gender = "male"
        if not customer['cu_gender']:
            gender = "female"

        customer['cu_gender'] = gender

        return {
            "u_id": customer['cu_id'],
            "u_name": customer['cu_name'],
            "u_email": customer['cu_email'],
            "u_image_url": customer['cu_image_url'],
            "u_gender": customer['cu_gender'],
            "u_role": customer['cu_role'],
            "u_created_on": customer['cu_created_on'],
        }
