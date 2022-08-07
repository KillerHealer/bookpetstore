import logging

import requests

from api.account_api import AccountApi
from models.account import Account
from models.token import Token

logger = logging.Logger
url = "https://bookstore.toolsqa.com/"
header = {'accept': 'application/json'}
my_book = {"isbn": 1, "title": "my_book", "subTitle": "my life", "author": "me", "publish_date": "1.1.2000",
           "publisher": "him", "pages": 200, "description": "cool book about me", "website": "www.google.com/me"}
my_user = {"userName": "nmpvsb", "password": "Abcd1234@"}
my_user_list = """[{"id": 10, "username": "Me", "firstName": "Noam", "lastName": "Barkai",
                 "email": "barkai@email.com", "password": "12345", "phone": "12345", "userStatus": 2},
                {"id": 11, "username": "theUser", "firstName": "John", "lastName": "James",
                 "email": "john@email.com", "password": "12345", "phone": "12345", "userStatus": 1}]"""
login = {"userName": "string", "password": "String123@"}
apiA = AccountApi()


def test_post_login_account():
    """
    tries to log in the user called 'login' and sees if it works
    :return:
    """
    logging.info("trying to login")
    response = apiA.post_login_authorized(login)
    assert response


def test_post_login_account_generate_token():
    """
    tries to get an authorized token for said account
    :return:
    """
    logging.info("trying to get a token")
    response = apiA.post_login_account_generate_token(login)
    logging.warning(f"{response}")
    assert isinstance(response, Token)


def test_post_new_user():
    """
    tries to create a new user and then tries to delete it for ease of use
    :return:
    """
    logging.info("trying to create a new user")
    response = apiA.post_new_user(my_user)
    assert isinstance(response, Account)
    logging.info("trying to delete the user i just created")
    response2 = requests.delete(f"{url}Account/v1/User/{response.userID}", headers=header)
    assert response2.status_code == 200


def test_delete_user():
    """
    tries to delete a user
    :return:
    """
    logging.info("trying to delete a user with a 30 character userID")
    ddid = "ca6fea99-bc81-4f06-9ada-14edb56cada1"
    response = apiA.delete_user(ddid)
    assert response.status_code == 200


