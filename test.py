import logging
import requests
from api.book_api import BookApi
from api.account_api import AccountApi
from book import Book
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
apiB = BookApi()


def test_post_login_account(params):
    """
    tries to log in the user called 'login' and sees if it works
    :return:
    """
    logging.info("trying to login")
    response = apiA.post_login_authorized(login, params["URL"])
    assert response


def test_post_login_account_generate_token(params):
    """
    tries to get an authorized token for said account
    :return:
    """
    logging.info("trying to get a token")
    response = apiA.post_login_account_generate_token(login, params["URL"])
    logging.warning(f"{response}")
    assert isinstance(response, Token)

# from here its not complete...


def test_post_new_user(params):
    """
    tries to create a new user and then tries to delete it for ease of use
    :return:
    """
    logging.info("trying to create a new user")
    response = apiA.post_new_user(my_user, params["URL"])
    assert isinstance(response, Account)
    logging.info("trying to delete the user i just created")
    response2 = requests.delete(f"{url}Account/v1/User/{response.userID}", headers=header)
    assert response2.status_code == 200


def test_delete_user(params):
    """
    tries to delete a user
    :return:
    """
    logging.info("trying to delete a user with a 30 character userID")
    ddid = "ca6fea99-bc81-4f06-9ada-14edb56cada1"
    response = apiA.delete_user(ddid, params["URL"])
    assert response.status_code == 200


def test_get_books(params):
    """
    tries to get all of the books in the store
    :param params:
    :return:
    """
    logging.info("trying to get a dictionary of books")
    books = apiB.get_books(params["URL"])
    assert isinstance(books, dict)


def test_post_books(params):
    """

    :param params:
    :return:
    """
