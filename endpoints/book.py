from fastapi import HTTPException

from server.application import app
from src.business_model.book.create_book import CreateBook
from src.business_model.book.delete_book import DeleteBook
from src.business_model.book.get_book import GetBook
from src.business_model.book.get_books import GetBooks
from src.business_model.book.update_book import UpdateBook
from src.core.response import Response
from view.book import IEditBook

CART_TAG = "Book"


@app.get("/book/all", tags=[CART_TAG])
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


@app.get("/book/{book_id}", tags=[CART_TAG])
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


@app.post("/book", tags=[CART_TAG])
def create_book(book: IEditBook):

    CreateBook(
        book=book
    ).run()

    return Response(
        access_token="",
        status_code=200,
        message="Success",
        content={}
    )


@app.put("/book/{book_id}", tags=[CART_TAG])
def update_book(book_id: int, book: IEditBook):
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


@app.delete('/book/{book_id}', tags=[CART_TAG])
def delete_book(book_id: int):
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
