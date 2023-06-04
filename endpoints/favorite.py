from fastapi import Depends
from pydantic import BaseModel

from server.application import app, oauth_schema
from src.business_model.auth.decode_token import DecodeToken
from src.business_model.favorite.create_favorite import CreateFavorite
from src.business_model.favorite.delete_favorites import DeleteFavorite
from src.business_model.favorite.get_favorite import GetFavorite
from src.business_model.favorite.get_favorites import GetFavorites


@app.get('/favorite/all', tags=["Favorite"])
def get_favorite(token: str = Depends(oauth_schema)):
    payload = DecodeToken(
        token=token
    ).run()

    favorites = GetFavorites(
        payload.customer_id
    ).run()

    return {
        "access_token": "",
        "message": "Success",
        "status_code": 200,
        "content": {
            "favorites": favorites
        }
    }


class ICreateFavorite(BaseModel):
    book_id: int


@app.post('/favorite', tags=["Favorite"])
def create_favorite(data: ICreateFavorite, token: str = Depends(oauth_schema)):
    payload = DecodeToken(
        token=token
    ).run()

    favorite = CreateFavorite(
        customer_id=payload.customer_id,
        book_id=data.book_id
    ).run()

    return {
        "access_token": "",
        "message": "Success",
        "status_code": 200,
        "content": {
            "favorite": favorite
        }
    }


@app.delete('/favorite/{favorite_id}', tags=["Favorite"])
def delete_favorite(favorite_id: int, token: str = Depends(oauth_schema)):
    payload = DecodeToken(
        token=token
    ).run()

    DeleteFavorite(
        favorite_id=favorite_id
    ).run()

    return {
        "access_token": "",
        "message": "Success",
        "status_code": 200,
        "content": {}
    }

