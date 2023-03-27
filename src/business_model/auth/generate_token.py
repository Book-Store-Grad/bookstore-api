import datetime

import jwt


class GenerateToken:
    def __init__(self, customer_id: int, role: str):
        self.customer_id = customer_id
        self.role = role

    def run(self) -> str:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=10),
            "cu_id": self.customer_id,
            "role": self.role
        }

        encoded_jwt = jwt.encode(
            payload,
            "secret",
            algorithm="HS256"
        )

        return encoded_jwt
