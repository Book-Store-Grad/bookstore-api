import os

from fastapi import HTTPException, Depends, File, UploadFile
from starlette.responses import FileResponse

from server.application import app, oauth_schema
from src.business_model.auth.decode_token import DecodeToken
from src.business_model.customer.get_customer import GetCustomer
from src.business_model.customer.get_image import GetCustomerImage
from src.business_model.customer.is_customer_exists import IsCustomerExists
from src.business_model.customer.update_customer import UpdateCustomer
from src.business_model.customer.upload_image import UploadImage
from src.core.response import Response
from src.interface.customer import IUpdateCustomer
from src.interface.token import IToken

CUSTOMER_TAG = "Customer"


@app.get('/customer/profile', tags=[CUSTOMER_TAG])
def get_customer(token: str = Depends(oauth_schema)):
    payload = DecodeToken(
        token=token
    ).run()

    exists = IsCustomerExists(
        customer_id=payload.customer_id
    )
    if not exists:
        raise HTTPException(
            detail="User does not exist",
            status_code=400
        )

    customer = GetCustomer(
        customer_id=payload.customer_id
    ).run()

    return Response(
        access_token="",
        status_code=200,
        message="",
        content={
            "customer": customer
        },
    )


@app.put("/customer/profile", tags=[CUSTOMER_TAG])
def update_customer(customer: IUpdateCustomer, token: str = Depends(oauth_schema)):
    payload = DecodeToken(
        token=token
    ).run()

    print("Payload: ", payload.__dict__)

    exists = IsCustomerExists(
        customer_id=payload.customer_id
    )
    if not exists:
        raise HTTPException(
            detail="User does not exist",
            status_code=400
        )

    customer = UpdateCustomer(
        customer=customer,
        customer_id=payload.customer_id
    ).run()

    return Response(
        access_token="",
        status_code=200,
        message="",
        content={
            "customer": customer
        },
    )


@app.post("/customer/image", tags=[CUSTOMER_TAG])
def update_image(image: UploadFile = File(...), token: str = Depends(oauth_schema)):
    payload = DecodeToken(
        token=token
    ).run()

    UploadImage(
        image=image,
        customer_id=payload.customer_id
    ).run()

    return Response(
        access_token=token,
        status_code=200,
        message="",
        content={},
    )


@app.get('/customer/image', tags=[CUSTOMER_TAG])
def get_image(token: str = Depends(oauth_schema)):
    payload = DecodeToken(
        token=token
    ).run()

    image_path = GetCustomerImage(
        customer_id=payload.customer_id
    ).run()

    return FileResponse(image_path)
