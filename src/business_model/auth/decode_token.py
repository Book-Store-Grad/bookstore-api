import datetime

import jwt

from src.interface.token import IToken


class DecodeToken:
    def __init__(self, token: str, strict: bool = True):
        self.token = token
        self.strict = strict

    def run(self) -> IToken:
        try:
            payload = jwt.decode(self.token, options={"verify_signature": False})
        except jwt.exceptions.DecodeError:
            if self.strict:
                raise jwt.exceptions.DecodeError()
            return IToken(
                token="",
                cu_id=0,
            )


        # TODO: Add Expiry Date Check

        customer_id = None
        try:
            customer_id = int(payload['cu_id'])
        except KeyError:
            pass

        return IToken(
            token=self.token,
            customer_id=customer_id,
        )
