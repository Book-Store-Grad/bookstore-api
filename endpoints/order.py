from fastapi import Depends

from server.application import app, oauth_schema
from src.business_model.auth.decode_token import DecodeToken
from src.business_model.order.create_order import CreateOrder
from src.business_model.order.get_order import GetOrder
from src.business_model.order.get_orders import GetOrders
from src.core.response import Response
from src.interface.order import IOrder

ORDER_TAG = "Order"


@app.post('/order', tags=[ORDER_TAG])
def create_order(token: str = Depends(oauth_schema)):
    payload = DecodeToken(
        token=token
    ).run()

    order = CreateOrder(
        order=IOrder(
            customer_id=payload.customer_id
        )
    ).run()

    return Response(
        access_token=token,
        message="Success",
        status_code=200,
        content={
            "order": order
        }
    )


@app.get('/order/all', tags=[ORDER_TAG])
def get_orders(token: str = Depends(oauth_schema)):
    payload = DecodeToken(
        token=token
    ).run()

    order = GetOrders(
        customer_id=payload.customer_id
    ).run()

    return Response(
        access_token=token,
        status_code=200,
        message="Success",
        content={
            "order": order
        }
    )


@app.get('/order/{order_id}', tags=[ORDER_TAG])
def get_order(order_id: int, token: str = Depends(oauth_schema)):
    order = GetOrder(
        order_id=order_id
    ).run()

    return Response(
        access_token=token,
        status_code=200,
        message="Success",
        content={
            "order": order
        }
    )
