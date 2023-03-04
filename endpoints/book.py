from fastapi import HTTPException
from pydantic import BaseModel

from server.application import app
from src.business_model.book.CreateBook import CreateBook
from src.business_model.book.DeleteBook import DeleteBook
from src.business_model.book.GetBook import GetBook
from src.business_model.book.GetBooks import GetBooks
from src.business_model.book.UpdateBook import UpdateBook
from src.core.response import Response
from view.book import IBook, IEditBook


@app.get("/book/all", tags=['Book'])
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


@app.get("/book/{book_id}", tags=['Book'])
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


@app.post("/book", tags=['Book'])
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


@app.put("/book/{book_id}", tags=['Book'])
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


@app.delete('/book/{book_id}', tags=['Book'])
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
