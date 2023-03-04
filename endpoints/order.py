from server.application import app
from src.interface.order import ICreateOrder, IGetOrders

ORDER_TAG = "Order"


@app.post('/order', tags=[ORDER_TAG])
def create_order(data: ICreateOrder):
    pass


@app.get('/order/all', tags=[ORDER_TAG])
def get_orders(data: IGetOrders):
    pass


@app.get('/order/{order_id}', tags=[ORDER_TAG])
def get_order(order_id: int):
    pass
