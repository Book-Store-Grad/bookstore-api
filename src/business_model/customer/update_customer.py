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

        gender = None
        if self.customer.gender.lower() in ["f", "female"]:
            gender = False
        elif self.customer.gender.lower() in ["m", "male"]:
            gender = True

        data = {}

        if self.customer.name:
            data["cu_name"] = self.customer.name

        if self.customer.gender and gender is not None:
            data['cu_gender'] = str(gender)

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

        return customer
