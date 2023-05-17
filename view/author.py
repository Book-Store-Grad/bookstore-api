from enum import Enum
from typing import List

from pydantic import BaseModel

from src.core.response import Response


class IEditAuthor(BaseModel):
    name: str


class IAuthor(BaseModel):
    id: int
    name: str


class GetAuthorsResponse(Response):
    content: dict
