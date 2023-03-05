import datetime

import jwt


class GenerateToken:
    def __init__(self, customer_id: int):
        self.customer_id = customer_id

    def run(self) -> str:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=10),
            "cu_id": self.customer_id,
        }

        encoded_jwt = jwt.encode(
            payload,
            "secret",
            algorithm="HS256"
        )

        return encoded_jwt
