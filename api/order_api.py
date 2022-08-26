import requests
from models.order import Order
from models.order import OrderStatus


class Inventory:
    def __init__(self, approved: int, delivered: int, placed: int = 0):
        self.placed = placed
        self.approved = approved
        self.delivered = delivered


class OrderApi:
    def __init__(self, url: str = "https://petstore3.swagger.io/api/v3/store"):
        self._url = url
        self._headers = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def get_inventory(self, url: str):
        if url is None:
            url = "https://petstore3.swagger.io/api/v3/store"
        res = self._session.get(url=f"{url}/inventory", headers=self._headers)
        inv = res.json()
        if res.status_code == 200:
            # inv["placed"] = inv.pop('') used to have a third parameter with no characters...
            my_inv = Inventory(**inv)
            return my_inv
        else:
            return res.status_code

    def post_new_order(self, order, url: str):
        if url is None:
            url = "https://petstore3.swagger.io/api/v3/store"
        order_data = order.to_json()
        res = self._session.post(url=f"{url}/order", data=order_data, headers=self._headers)
        o1 = res.json()
        if res.status_code == 200:
            my_order = Order(**o1)
            return my_order
        else:
            return res.status_code

    def get_order_by_id(self, id, url: str):
        if url is None:
            url = "https://petstore3.swagger.io/api/v3/store"
        res = self._session.get(url=f"{url}/order/{id}", headers=self._headers)
        o1 = res.json()
        if res.status_code == 200:
            my_order = Order(**o1)
            return my_order
        else:
            return res.status_code

    def delete_order_by_id(self, id, url: str):
        if url is None:
            url = "https://petstore3.swagger.io/api/v3/store"
        res = self._session.delete(url=f"{url}/order/{id}", headers=self._headers)
        if res.status_code == 200:
            res = self._session.get(url=f"{url}/order/{id}", headers=self._headers)
            if res.status_code == 200:
                o1 = res.json()
                my_order = Order(**o1)
                return my_order
            else:
                return res.status_code
