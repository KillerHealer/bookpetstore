import requests
from models.book import Book


class BookApi:
    def __init__(self, url="https://bookstore.toolsqa.com/BookStore/v1/Book"):
        self._url = url
        self._headers = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def get_books(self):
        res = self._session.get(f"{self._url}s", headers=self._headers)
        if res.status_code != 200:
            mm = res.json()
            my_mm = MessageModel(**mm)
            return my_mm
        else:
            return dict(res)

    def post_books(self):
        res = self._session.post(f"{self._url}s", headers=self._headers)
        if res.status_code != 200:
            mm = res.json()
            my_mm = MessageModel(**mm)
            return my_mm
        else:
            return dict(res)

    def delete_books(self):
        res = self._session.delete(f"{self._url}s", headers=self._headers)
        if res.status_code != 200:
            mm = res.json()
            my_mm = MessageModel(**mm)
            return my_mm
        else:
            return dict(res)