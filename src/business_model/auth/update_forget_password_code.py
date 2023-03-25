import random

from src.business_model.email.SendEmail import SendEmail
from src.core.business_model import BusinessModel, ModelType
from src.data_model.customer import Customer


class UpdateForgetPasswordCode(BusinessModel):
    def __init__(self, customer: dict):
        super().__init__(
            model=Customer(),
            model_type=ModelType.update
        )

        self.customer = customer

    def run(self, data: dict = None, conditions: dict = None):
        code = random.randrange(1000, 9999)

        print("code: ", code)

        print("customer: ", self.customer)

        is_email_sent = SendEmail(
            email="bookstoreapi052@gmail.com",
            # password="191319712345"
            password="scimqczuqdpevzau"
        ).send_email(
            to=self.customer["cu_email"],
            subject="Forget Password",
            contents="Your code is: " + str(code)
        )

        if not is_email_sent:
            return False

        self.model.update(
            conditions={
                "cu_id": {
                    "$value": int(self.customer['cu_id'])
                }
            },
            data={
                "cu_pw_code": str(code)
            }
        ).commit()

        return code
