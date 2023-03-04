from fastapi import HTTPException
from pydantic import BaseModel

from server.application import app
from src.business_model.auth.sign_in import SignIn
from src.business_model.customer.create_customer import CreateCustomer
from src.business_model.customer.is_customer_exists_by_email import IsCustomerExistsByEmail
from src.core.response import Response
from src.interface.customer import ICustomer


class ISignIn(BaseModel):
    email: str
    password: str


class ISignUp(BaseModel):
    name: str
    email: str
    password: str
    gender: bool


class IResetPassword(BaseModel):
    reset_token: str


class IForgetPassword(BaseModel):
    email: str


AUTHENTICATION_TAG = 'Authentication'


@app.post('/auth/signin', tags=[AUTHENTICATION_TAG])
def signin(user: ISignIn):

    customer = SignIn(
        email=user.email,
        password=user.password,
    ).run()

    return Response(
        access_token="",
        status_code=200,
        message="",
        content={
            "customer": customer
        },
    )


@app.post('/auth/signup', tags=[AUTHENTICATION_TAG])
def signup(user: ISignUp):
    exists = IsCustomerExistsByEmail(
        email=user.email
    ).run()

    if exists:
        raise HTTPException(
            detail="Customer Already Exists",
            status_code=400
        )

    customer = CreateCustomer(
        customer=ICustomer(**user.__dict__)
    ).run()

    return Response(
        access_token="",
        status_code=200,
        message="",
        content={
            "customer": customer
        },
    )


@app.post('/auth/forget-password', tags=[AUTHENTICATION_TAG])
def forget_password(data: IForgetPassword):
    return data.__dict__


@app.post('/auth/reset-password', tags=[AUTHENTICATION_TAG])
def reset_password(data: IResetPassword):
    return data.__dict__

