import requests
from models.account import Account
from models.message_model import MessageModel
from models.token import Token


class AccountApi:
    def __init__(self, url="https://bookstore.toolsqa.com/Account/v1"):
        self._url = url
        self._headers = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def post_login_authorized(self, login) -> MessageModel or bool:
        res = self._session.post(f"{self._url}/Authorized", data=login, headers=self._headers)
        if res.status_code != 200:
            mm = res.json()
            my_mm = MessageModel(**mm)
            return my_mm
        else:
            return bool(res)

    def post_login_account_generate_token(self, login) -> Token or MessageModel:
        res = self._session.post(f"{self._url}/GenerateToken", data=login, headers=self._headers)
        if res.status_code == 200:
            token = Token(**res.json())
            return token
        else:
            my_mm = MessageModel(**res.json())
            return my_mm

    def post_new_user(self, user):
        res = self._session.post(f"{self._url}/User", data=user, headers=self._headers)
        if res.status_code == 201:
            my_user = Account(**res.json())
            return my_user
        else:
            my_mm = MessageModel(**res.json())
            return my_mm

    def delete_user(self, uid: str):
        res = self._session.delete(f"{self._url}/User/{uid}", headers=self._headers)
        if res.status_code == 200:
            mm = res.json()
            my_mm = MessageModel(**mm)
            return my_mm
        else:
            return res.status_code

    def get_user(self, uid):
        res = self._session.get(f"{self._url}/User/{uid}", headers=self._headers)
        if res.status_code == 200:
            user = Account(**res.json())
            return user
        else:
            return res.status_code