from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth_schema = OAuth2PasswordBearer(tokenUrl='auth')
