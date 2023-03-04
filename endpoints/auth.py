from pydantic import BaseModel

from server.application import app


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
    return user.__dict__


@app.post('/auth/signup', tags=[AUTHENTICATION_TAG])
def signup(user: ISignUp):
    return user.__dict__


@app.post('/auth/forget-password', tags=[AUTHENTICATION_TAG])
def forget_password(data: IForgetPassword):
    return data.__dict__


@app.post('/auth/reset-password', tags=[AUTHENTICATION_TAG])
def reset_password(data: IResetPassword):
    return data.__dict__

