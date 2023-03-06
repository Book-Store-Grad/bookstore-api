from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from server.application import app, oauth_schema
from src.business_model.auth.UpdateForgetPasswordCode import UpdateForgetPasswordCode
from src.business_model.auth.generate_token import GenerateToken
from src.business_model.auth.sign_in import SignIn
from src.business_model.customer.create_customer import CreateCustomer
from src.business_model.customer.get_customer_by_email import GetCustomerByEmail
from src.business_model.customer.is_customer_exists_by_email import IsCustomerExistsByEmail
from src.core.response import Response
from src.interface.customer import ICustomer


class ISignIn(OAuth2PasswordRequestForm):
    username: str
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


@app.post('/auth', tags=[AUTHENTICATION_TAG])
def signin(user: ISignIn = Depends()):
    exists = IsCustomerExistsByEmail(
        email=user.username
    ).run()

    if not exists:
        raise HTTPException(
            detail="Customer does not exist",
            status_code=400
        )

    customer = SignIn(
        email=user.username,
        password=user.password,
    ).run()

    token = GenerateToken(
        customer_id=customer['cu_id'],
    ).run()

    return Response(
        access_token=token,
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

    token = GenerateToken(
        customer_id=customer['cu_id'],
    ).run()

    return Response(
        access_token=token,
        status_code=200,
        message="Success",
        content={
            "customer": customer
        },
    )


@app.post('/auth/forget-password', tags=[AUTHENTICATION_TAG])
def forget_password(data: IForgetPassword):
    customer_id = GetCustomerByEmail(
        email=data.email
    ).run()['cu_id']

    forget_code = UpdateForgetPasswordCode(
        customer_id=customer_id
    ).run()

    return Response(
        access_token="",
        status_code=200,
        message="Success",
        content={
            "code": forget_code
        }
    )


@app.post('/auth/reset-password', tags=[AUTHENTICATION_TAG])
def reset_password(data: IResetPassword, token: str = Depends(oauth_schema)):
    return Response(
        access_token=token,
        status_code=200,
        message="Success",
        content={}
    )
