import json
import pytest
import logging
import requests


url = "https://bookstore.toolsqa.com/"
header = {'accept': 'application/json'}
my_book = {"isbn": 1, "title": "my_book", "subTitle": "my life", "author": "me", "publish_date": "1.1.2000",
           "publisher": "him", "pages": 200, "description": "cool book about me", "website": "www.google.com/me"}
my_user = {"userName": "k", "password": "Abcd1234@"}
my_user_list = """[{"id": 10, "username": "Me", "firstName": "Noam", "lastName": "Barkai",
                 "email": "barkai@email.com", "password": "12345", "phone": "12345", "userStatus": 2},
                {"id": 11, "username": "theUser", "firstName": "John", "lastName": "James",
                 "email": "john@email.com", "password": "12345", "phone": "12345", "userStatus": 1}]"""
login = {"userName": "string", "password": "String123@"}


def test_post_login_account():
    response = requests.post(f"{url}Account/v1/Authorized", data=login, headers=header)
    assert response.status_code == 200


def test_post_login_account_generate_token():
    response = requests.post(f"{url}Account/v1/GenerateToken", data=login, headers=header)
    assert response.status_code == 200


def test_post_new_user():
    response = requests.post(f"{url}Account/v1/User", data=my_user, headers=header)
    assert response.status_code == 201
    ddid = ""
    for char in list(response.text.split(":")[1]):
        if char == '"':
            continue
        if char == ",":
            break
        ddid += char
    response2 = requests.delete(f"{url}Account/v1/User/{ddid}", headers=header)
    assert response2.status_code == 200
