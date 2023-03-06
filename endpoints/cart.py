from fastapi import HTTPException, Depends

from server.application import app, oauth_schema
from src.business_model.auth.decode_token import DecodeToken
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
def get_cart_items(token: str = Depends(oauth_schema)):
    payload = DecodeToken(
        token=token
    ).run()

    items = GetCartItems(
        payload.customer_id
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
def get_cart_item(cart_item_id: int, token: str = Depends(oauth_schema)):
    payload = DecodeToken(
        token=token
    ).run()

    item = GetCartItem(
        payload.customer_id,
        cart_item_id=cart_item_id
    ).run()

    return Response(
        access_token="",
        message="",
        status_code=200,
        content={
            "cart_item": item or {}
        }
    )


@app.post("/cart", tags=[CART_TAG])
def add_to_cart(data: IAddToCart, token: str = Depends(oauth_schema)):
    payload = DecodeToken(
        token=token
    ).run()

    is_customer_exists = IsCustomerExists(
        customer_id=payload.customer_id
    ).run()

    if not is_customer_exists:
        raise HTTPException(
            detail="Customer Id does not exist",
            status_code=400
        )

    AddToCart(
        customer_id=payload.customer_id,
        book_id=data.book_id,
    ).run()

    items = GetCartItems(
        customer_id=payload.customer_id
    ).run()

    return Response(
        access_token="",
        message="",
        status_code=200,
        content={
            "cart_items": items
        },
    )


@app.delete("/cart/{cart_item_id}", tags=[CART_TAG])
def remove_to_cart(cart_item_id: int, token: str = Depends(oauth_schema)):
    payload = DecodeToken(
        token=token
    ).run()

    RemoveFromCart(
        cart_item_id=cart_item_id,
        customer_id=payload.customer_id
    ).run()

    return Response(
        access_token="",
        message="",
        status_code=200,
        content={},
    )
