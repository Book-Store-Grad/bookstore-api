from pydantic import BaseModel

from server.application import app


class ISignIn(BaseModel):
    pass


@app.post('/', tags=['Authentication'])
def signin(user: ISignIn):
    pass
