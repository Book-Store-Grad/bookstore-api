import datetime

import jwt


class GenerateToken:
    def __init__(self, user_id, vendor: dict = None):
        self.user_id = user_id
        self.vendor = vendor

    def run(self):
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=10),
            "cu_id": self.user_id,
        }

        encoded_jwt = jwt.encode(
            payload,
            "secret",
            algorithm="HS256"
        )

        return encoded_jwt
