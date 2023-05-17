from fastapi import HTTPException, Depends

from server.application import app, oauth_schema
from src.business_model.auth.decode_token import DecodeToken
from src.business_model.author.create_author import CreateAuthor
from src.business_model.author.delete_author import DeleteAuthor
from src.business_model.author.get_author import GetAuthor
from src.business_model.author.get_authors import GetAuthors
from src.business_model.author.update_author import UpdateAuthor
from src.core.response import Response
from view.author import IEditAuthor

TAG = "Author"


@app.get("/author/all", tags=[TAG])
def get_all_authors(query: str = None):

    authors = GetAuthors(
        query=query
    ).run()

    return Response(
        access_token="",
        status_code=200,
        message="",
        content={
            "authors": authors,
        }
    )


@app.get("/author/{author_id}", tags=[TAG])
def get_author(author_id: int):
    try:
        author_id = int(author_id)
    except:
        raise HTTPException(
            detail="Author id must be a valid int",
            status_code=400
        )

    authors = GetAuthor(
        int(author_id)
    ).run()

    return Response(
        access_token="",
        status_code=200,
        message="",
        content={
            "author": authors,
        }
    )


@app.post("/author", tags=[TAG])
def create_author(author: IEditAuthor, token: str = Depends(oauth_schema)):
    payload = DecodeToken(
        token
    ).run()

    print("Payload:", payload)

    if payload.role.lower() != 'author':
        raise HTTPException(
            detail="User not authorized",
            status_code=401
        )

    author = CreateAuthor(
        author=author
    ).run()

    return Response(
        access_token="",
        status_code=200,
        message="Success",
        content={
            "author": author,
        },
    )


@app.put("/author/{author_id}", tags=[TAG])
def update_author(author_id: int, author: IEditAuthor, token: str = Depends(oauth_schema)):
    payload = DecodeToken(
        token
    ).run()

    print("Payload:", payload)

    if payload.role.lower() != 'author':
        raise HTTPException(
            detail="User not authorized",
            status_code=401
        )

    try:
        author_id = int(author_id)
    except:
        raise HTTPException(
            detail="Author id must be a valid int",
            status_code=400
        )

    try:
        author = UpdateAuthor(
            author_id=author_id,
            author=author
        ).run()
    except Exception as e:
        raise HTTPException(
            detail=str(e),
            status_code=400
        )

    return Response(
        access_token="",
        status_code=200,
        message="Success",
        content=author
    )


@app.delete('/author/{author_id}', tags=[TAG])
def delete_author(author_id: int, token: str = Depends(oauth_schema)):
    payload = DecodeToken(
        token
    ).run()

    print("Payload:", payload)

    if payload.role.lower() != 'author':
        raise HTTPException(
            detail="User not authorized",
            status_code=401
        )

    try:
        author_id = int(author_id)
    except:
        raise HTTPException(
            detail="Author Id must be a valid int",
            status_code=400
        )

    DeleteAuthor(
        author_id=author_id
    ).run()

    return Response(
        access_token="",
        status_code=200,
        message="Success",
        content={},
    )

