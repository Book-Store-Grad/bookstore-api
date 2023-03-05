import os

from fastapi import HTTPException, Depends
from starlette.responses import FileResponse

from server.application import app, oauth_schema
from src.business_model.auth.decode_token import DecodeToken
from src.business_model.customer.get_customer import GetCustomer
from src.business_model.customer.is_customer_exists import IsCustomerExists
from src.core.response import Response
from src.interface.token import IToken

CUSTOMER_TAG = "Customer"


@app.get('/customer/profile', tags=[CUSTOMER_TAG])
def get_customer(token: str = Depends(oauth_schema)):
    payload = DecodeToken(
        token=token
    ).run()

    exists = IsCustomerExists(
        customer_id=payload.cu_id
    )
    if not exists:
        raise HTTPException(
            detail="Customer does not exist",
            status_code=400
        )

    customer = GetCustomer(
        customer_id=payload.cu_id
    ).run()

    return Response(
        access_token="",
        status_code=200,
        message="",
        content={
            "customer": customer
        },
    )


@app.get('/customer/image', tags=[CUSTOMER_TAG])
def get_image(token: str = Depends(oauth_schema)):
    payload = DecodeToken(
        token=token
    ).run()
    # TODO: Get Image path
    return FileResponse("")
