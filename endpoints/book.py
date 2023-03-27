from fastapi import HTTPException, UploadFile, File, Depends
from starlette.responses import FileResponse

from server.application import app, oauth_schema
from src.business_model.auth.decode_token import DecodeToken
from src.business_model.book.create_book import CreateBook
from src.business_model.book.delete_book import DeleteBook
from src.business_model.book.get_book import GetBook
from src.business_model.book.get_books import GetBooks
from src.business_model.book.get_file import GetBookFile
from src.business_model.book.get_image import GetBookImage
from src.business_model.book.update_book import UpdateBook
from src.business_model.book.upload_file import UploadBookFile
from src.business_model.book.upload_image import UploadImage
from src.core.response import Response
from view.book import IEditBook

TAG = "Book"


@app.get("/book/all", tags=[TAG])
def get_all_books():
    books = GetBooks().run()

    return Response(
        access_token="",
        status_code=200,
        message="",
        content={
            "books": books,
        }
    )


@app.get("/book/{book_id}/image", tags=[TAG])
def get_book_image(book_id: int):
    try:
        book_id = int(book_id)
    except:
        raise HTTPException(
            detail="Book id must be a valid int",
            status_code=400
        )

    image = GetBookImage(
        book_id=book_id
    ).run()

    if image is None:
        raise HTTPException(
            detail="Book image does not exist",
            status_code=404
        )

    try:
        return FileResponse(
            image,
        )
    except:
        raise HTTPException(
            detail="Book image does not exist",
            status_code=404
        )


@app.get("/book/{book_id}/file", tags=[TAG])
def get_book_file(book_id: int):
    try:
        book_id = int(book_id)
    except:
        raise HTTPException(
            detail="Book id must be a valid int",
            status_code=400
        )

    image = GetBookFile(
        book_id=book_id
    ).run()

    if image is None:
        raise HTTPException(
            detail="Book file does not exist",
            status_code=404
        )

    try:
        return FileResponse(
            image,
        )
    except:
        raise HTTPException(
            detail="Book file does not exist",
            status_code=404
        )


@app.get("/book/{book_id}", tags=[TAG])
def get_book(book_id: int):
    try:
        book_id = int(book_id)
    except:
        raise HTTPException(
            detail="Book id must be a valid int",
            status_code=400
        )

    books = GetBook(
        int(book_id)
    ).run()

    return Response(
        access_token="",
        status_code=200,
        message="",
        content={
            "book": books,
        }
    )


@app.post("/book", tags=[TAG])
def create_book(book: IEditBook, token: str = Depends(oauth_schema)):
    payload = DecodeToken(
        token
    ).run()

    print("Payload:", payload)

    if payload.role.lower() != 'author':
        raise HTTPException(
            detail="User not authorized",
            status_code=401
        )

    CreateBook(
        book=book
    ).run()

    return Response(
        access_token="",
        status_code=200,
        message="Success",
        content={}
    )


@app.post("/book/{book_id}/file", tags=[TAG])
def upload_book_file(book_id: int, file: UploadFile = File(...)):
    try:
        book_id = int(book_id)
    except:
        raise HTTPException(
            detail="Book id must be a valid int",
            status_code=400
        )

    print("File:", file.filename)
    print("File:", file.content_type)

    if file.content_type != "application/pdf":
        raise HTTPException(
            detail="File must be a pdf",
            status_code=400
        )

    UploadBookFile(
        book_id=book_id,
        file=file
    ).run()

    return Response(
        access_token="",
        status_code=200,
        message="Success",
        content={}
    )


@app.post("/book/{book_id}/image", tags=[TAG])
def upload_book_image(book_id: int, image: UploadFile = File(...)):
    try:
        book_id = int(book_id)
    except:
        raise HTTPException(
            detail="Book id must be a valid int",
            status_code=400
        )

    print("Image:", image.filename)
    print("Image:", image.content_type)

    UploadImage(
        book_id=book_id,
        image=image
    ).run()

    return Response(
        access_token="",
        status_code=200,
        message="Success",
        content={}
    )


@app.put("/book/{book_id}", tags=[TAG])
def update_book(book_id: int, book: IEditBook, token: str = Depends(oauth_schema)):
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
        book_id = int(book_id)
    except:
        raise HTTPException(
            detail="Book id must be a valid int",
            status_code=400
        )

    book = UpdateBook(
        book_id=book_id,
        book=book
    ).run()

    return Response(
        access_token="",
        status_code=200,
        message="Success",
        content=book
    )


@app.delete('/book/{book_id}', tags=[TAG])
def delete_book(book_id: int, token: str = Depends(oauth_schema)):
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
        book_id = int(book_id)
    except:
        raise HTTPException(
            detail="Book Id must be a valid int",
            status_code=400
        )

    DeleteBook(
        book_id=book_id
    ).run()

    return Response(
        access_token="",
        status_code=200,
        message="Success",
        content={},
    )
