import requests
import pytest
from models.book import Book
from models.message_model import MessageModel


class BookApi:
    def __init__(self, url="https://bookstore.toolsqa.com/BookStore/v1/Book"):
        self._url = url
        self._headers = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def get_books(self, url="https://bookstore.toolsqa.com/BookStore/v1/Book"):
        res = self._session.get(f"{url}s", headers=self._headers)
        if res.status_code != 200:
            mm = res.json()
            my_mm = MessageModel(**mm)
            return my_mm
        else:
            return dict(res)

    def post_books(self, url="https://bookstore.toolsqa.com/BookStore/v1/Book"):
        res = self._session.post(f"{url}s", headers=self._headers)
        if res.status_code != 200:
            mm = res.json()
            my_mm = MessageModel(**mm)
            return my_mm
        else:
            return dict(res)

    def delete_books(self, url="https://bookstore.toolsqa.com/BookStore/v1/Book"):
        res = self._session.delete(f"{url}s", headers=self._headers)
        if res.status_code != 200:
            mm = res.json()
            my_mm = MessageModel(**mm)
            return my_mm
        else:
            return dict(res)
