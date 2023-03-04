from fastapi import HTTPException

from server.application import app
from src.business_model.customer.get_customer import GetCustomer
from src.business_model.customer.is_customer_exists import IsCustomerExists
from src.core.response import Response
from src.interface.token import IToken

CUSTOMER_TAG = "Customer"


@app.get('/profile', tags=[CUSTOMER_TAG])
def get_customer():
    token = IToken(
        token="dfghj",
        cu_id=3,
    )

    exists = IsCustomerExists(
        customer_id=token.cu_id
    )
    if not exists:
        raise HTTPException(
            detail="Customer does not exist",
            status_code=400
        )

    customer = GetCustomer(
        customer_id=token.cu_id
    ).run()

    return Response(
        access_token="",
        status_code=200,
        message="",
        content={
            "customer": customer
        },
    )
