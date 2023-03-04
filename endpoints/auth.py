from pydantic import BaseModel

from server.application import app


class ISignIn(BaseModel):
    pass


class ISignUp(BaseModel):
    pass


class IResetPassword(BaseModel):
    pass


AUTHENTICATION_TAG = 'Authentication'


@app.post('/auth/signin', tags=[AUTHENTICATION_TAG])
def signin(user: ISignIn):
    pass


@app.post('/auth/signup', tags=[AUTHENTICATION_TAG])
def signup(user: ISignUp):
    pass


@app.post('/auth/forget-password', tags=[AUTHENTICATION_TAG])
def forget_password(email: str):
    pass


@app.post('/auth/reset-password', tags=[AUTHENTICATION_TAG])
def reset_password(data: IResetPassword):
    pass
