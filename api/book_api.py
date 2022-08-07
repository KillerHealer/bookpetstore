import requests
from models.book import Book


class BookApi:
    def __init__(self, url="https://bookstore.toolsqa.com/BookStore/v1/Book"):
        self._url = url
        self._headers = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers.update(self._headers)

