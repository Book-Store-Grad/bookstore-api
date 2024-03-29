from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from server.application import app, oauth_schema
from src.business_model.auth.decode_token import DecodeToken
from src.business_model.auth.reset_password import ResetPassword
from src.business_model.auth.update_forget_password_code import UpdateForgetPasswordCode
from src.business_model.auth.generate_token import GenerateToken
from src.business_model.auth.sign_in import SignIn
from src.business_model.auth.update_reset_field import UpdateResetField
from src.business_model.customer.create_customer import CreateCustomer
from src.business_model.customer.get_customer_by_email import GetCustomerByEmail
from src.business_model.customer.get_customer_by_password_code import GetCustomerByPasswordCode
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
    gender: str
    role: str = "customer"


class IResetPassword(BaseModel):
    code: str
    password: str


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
            detail="User does not exist",
            status_code=400
        )

    customer = SignIn(
        email=user.username,
        password=user.password,
    ).run()

    if customer is None:
        raise HTTPException(
            detail="Wrong password",
            status_code=400
        )

    token = GenerateToken(
        customer_id=customer['u_id'],
        role=str(customer['u_role']).lower()
    ).run()

    return Response(
        access_token=token,
        status_code=200,
        message="",
        content={
            "user": customer
        },
    )


@app.post('/auth/signup', tags=[AUTHENTICATION_TAG])
def signup(user: ISignUp):

    print("User:", user.__dict__)

    if user.role not in ['customer', 'author']:
        raise HTTPException(
            detail="Role must be either customer or author",
            status_code=400
        )

    exists = IsCustomerExistsByEmail(
        email=user.email
    ).run()

    if exists:
        raise HTTPException(
            detail="User Already Exists",
            status_code=400
        )

    try:
        customer = CreateCustomer(
            customer=ICustomer(**user.__dict__)
        ).run()
    except Exception as error_message:
        print("error_message: ", error_message)
        raise HTTPException(
            detail="User Creation Failed: {}".format(error_message),
            status_code=422
        )

    token = GenerateToken(
        customer_id=customer['u_id'],
        role=customer['u_role']
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
    customer = GetCustomerByEmail(
        email=data.email
    ).run()

    print("Email: ", data.email, "Customer: ", customer)

    try:
        customer_id = customer['cu_id']
    except Exception as error_message:
        raise HTTPException(
            detail="User does not exist",
            status_code=422
        )

    forget_code = UpdateForgetPasswordCode(
        customer=customer
    ).run()

    if forget_code is False:
        raise HTTPException(
            detail="Forget Password Failed",
            status_code=400
        )

    UpdateResetField(
        customer_id=customer_id,
        value=True
    )

    return Response(
        access_token="",
        status_code=200,
        message="Success",
        content={
            "code": forget_code
        }
    )


@app.post('/auth/reset-password', tags=[AUTHENTICATION_TAG])
def reset_password(data: IResetPassword, ):
    customer = GetCustomerByPasswordCode(
        code=data.code
    ).run()

    reset = ResetPassword(
        code=data.code,
        password=data.password,
        customer_id=customer['cu_id'],
    ).run()

    if reset is not True:
        raise HTTPException(
            detail="Reset Password Failed",
            status_code=400
        )

    return Response(
        access_token="",
        status_code=200,
        message="Success",
        content={}
    )
