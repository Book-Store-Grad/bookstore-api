from fastapi import HTTPException

from server.application import app
from src.business_model.cart.add_to_cart import AddToCart
from src.business_model.cart.get_cart_item import GetCartItem
from src.business_model.cart.get_cart_items import GetCartItems
from src.business_model.cart.remove_from_cart import RemoveFromCart
from src.business_model.customer.is_customer_exists import IsCustomerExists
from src.core.response import Response
from src.interface.cart import IAddToCart
from src.interface.token import IToken

CART_TAG = "Cart"


@app.get('/cart/all', tags=[CART_TAG])
def get_cart_items():

    payload = IToken(
        token="ghjkl",
        cu_id=1,
    )

    items = GetCartItems(
        payload.cu_id
    ).run()

    return Response(
        access_token="",
        message="",
        status_code=200,
        content={
            "cart_items": items
        }
    )


@app.get('/cart/{cart_item_id}', tags=[CART_TAG])
def get_cart_item(cart_item_id: int):

    payload = IToken(
        token="ghjkl",
        cu_id=1,
    )

    item = GetCartItem(
        payload.cu_id,
        cart_item_id=cart_item_id
    ).run()

    return Response(
        access_token="",
        message="",
        status_code=200,
        content={
            "cart_item": item
        }
    )


@app.post("/cart", tags=[CART_TAG])
def add_to_cart(data: IAddToCart):

    is_customer_exists = IsCustomerExists(
        customer_id=data.customer_id
    ).run()

    if not is_customer_exists:
        raise HTTPException(
            detail="Customer Id does not exist",
            status_code=400
        )

    AddToCart(
        customer_id=data.customer_id,
        book_id=data.book_id,
    ).run()

    return Response(
        access_token="",
        message="",
        status_code=200,
        content={},
    )


@app.delete("/cart/{cart_item_id}", tags=[CART_TAG])
def remove_to_cart(cart_item_id: int):
    RemoveFromCart(
        cart_item_id=cart_item_id,
    ).run()

    return Response(
        access_token="",
        message="",
        status_code=200,
        content={},
    )

