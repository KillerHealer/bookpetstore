import json
from models.baseObj import baseObj
from enum import Enum


class OrderStatus(Enum):
    placed = "placed"
    approved = "approved"
    delivered = "delivered"


class Order(baseObj):
    def __init__(self, id: int, petId: int, quantity: int, shipDate: str, status: OrderStatus, complete: bool = False):
        self._id = id
        self._petId = petId
        self._quantity = quantity
        self._shipDate = shipDate
        self._status = status
        self._complete = complete

    @property
    def id(self):
        """Gets the id of this Order.
        :return: The id of this Order.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Order.
        :param id: The id of this Order.
        :type: int
        """
        self._id = id

    @property
    def petId(self):
        """Gets the petId of this Order.
        :return: The petId of this Order.
        :rtype: int
        """
        return self._petId

    @petId.setter
    def petId(self, petId):
        """Sets the petId of this Order.
        :param petId: The petId of this Order.
        :type: int
        """
        self._petId = petId

    @property
    def quantity(self):
        """Gets the quantity of this Order.
        :return: The quantity of this Order.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Order.
        :param quantity: The quantity of this Order.
        :type: int
        """
        self._quantity = quantity

    @property
    def shipDate(self):
        """Gets the shipDate of this Order.
        :return: The shipDate of this Order.
        :rtype: str
        """
        return self._shipDate

    @shipDate.setter
    def shipDate(self, shipDate):
        """Sets the shipDate of this Order.
        :param shipDate: The shipDate of this Order.
        :type: str
        """
        self._shipDate = shipDate

    @property
    def status(self):
        """Gets the status of this Order.
        :return: The status of this Order.
        :rtype: OrderStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Order.
        :param status: The status of this Order.
        :type: OrderStatus
        """
        self._status = status

    @property
    def complete(self):
        """Gets the complete status of this Order.
        :return: The complete status of this Order.
        :rtype: bool
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """Sets the complete status of this Order.
        :param complete: The complete status of this Order.
        :type: bool
        """
        self._complete = complete
