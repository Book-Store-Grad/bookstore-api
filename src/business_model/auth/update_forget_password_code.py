import random

from src.business_model.email.SendEmail import SendEmail
from src.core.business_model import BusinessModel, ModelType
from src.data_model.customer import Customer


class UpdateForgetPasswordCode(BusinessModel):
    def __init__(self, customer_id: int):
        super().__init__(
            model=Customer(),
            model_type=ModelType.update
        )

        self.customer_id = customer_id

    def run(self, data: dict = None, conditions: dict = None):
        code = random.randrange(1000, 9999)

        print("code: ", code)

        customer = self.model.get(
            condition={
                "cu_id": {
                    "$value": int(self.customer_id)
                }
            }
        ).get_one().show(True).result

        print("customer: ", customer)

        is_email_sent = SendEmail(
            email="",
            password=""
        ).send_email(
            to=customer["cu_email"],
            subject="Forget Password",
            contents="Your code is: " + str(code)
        )

        if not is_email_sent:
            return False

        self.model.update(
            conditions={
                "cu_id": {
                    "$value": int(self.customer_id)
                }
            },
            data={
                "cu_pw_code": str(code)
            }
        ).commit()

        return code
