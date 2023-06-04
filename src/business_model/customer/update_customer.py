from src.core.business_model import BusinessModel, ModelType
from src.data_model.customer import Customer
from src.interface.customer import IUpdateCustomer


class UpdateCustomer(BusinessModel):
    def __init__(self, customer_id: int, customer: IUpdateCustomer):
        super().__init__(
            model=Customer(),
            model_type=ModelType.update
        )

        self.customer = customer
        self.customer_id = customer_id

    def run(self, data: dict = None, conditions: dict = None) -> dict:

        data = {}

        gender = None
        if self.customer.gender:
            if self.customer.gender.lower() in ["f", "female"]:
                gender = False
            elif self.customer.gender.lower() in ["m", "male"]:
                gender = True

            if gender is not None:
                data['cu_gender'] = str(gender)

        if self.customer.name:
            data["cu_name"] = self.customer.name

        print("Customer Id: ", self.customer_id, "data: ", data)

        customer = super().run(
            data=data,
            conditions={
                "cu_id": {
                    "$value": str(self.customer_id)
                }
            }
        ).result

        customer.pop("cu_password", None)
        customer.pop("cu_pw_code", None)

        return {
            "u_id": customer['cu_id'],
            "u_name": customer['cu_name'],
            "u_email": customer['cu_email'],
            "u_image_url": customer['cu_image_url'],
            "u_gender": customer['cu_gender'],
            "u_role": customer['cu_role'],
            "u_created_on": customer['cu_created_on'],
        }
