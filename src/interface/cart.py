from pydantic import BaseModel


class IAddToCart(BaseModel):
    book_id: int
