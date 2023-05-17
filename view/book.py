from enum import Enum
from typing import List

from pydantic import BaseModel

from src.core.response import Response


class Genre(Enum):
    ABC = "ABC"


class IEditBook(BaseModel):
    name: str
    description: str
    genre: str
    author_id: int
    price: str


class IBook(BaseModel):
    id: int
    name: str
    description: str
    genre: str
    price: float


class GetBooksResponse(Response):
    content: dict
