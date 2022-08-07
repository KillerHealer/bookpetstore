import requests
from models.account import Account
from models.message_model import MessageModel


class AccountApi:
    def __init__(self, url="https://bookstore.toolsqa.com/Account/v1"):
        self._url = url
        self._headers = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def post_login_authorized(self, login):
        res = self._session.post(f"{self._url}/Authorized", data=login, headers=self._headers)
        if res.status_code != 200:
            mm = res.json()
            my_mm = MessageModel(**mm)
            return my_mm
        else:
            return bool(res)

    def post_login_account_generate_token(self, login):
        res = self._session.post(f"{self._url}/GenerateToken", data=login, headers=self._headers)
        