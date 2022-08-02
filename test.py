import json
import pytest
import logging
import requests
from api import pet_api

url = "https://petstore3.swagger.io/api/v3"
header = {'accept': 'application/json'}
dog_category = {"id": 1, "name": "Dogs"}
my_dog = {"id": 1, "name": "my_dog", "category": dog_category, "status": "available"}
my_user = {"id": 10, "username": "Me", "firstName": "Noam", "lastName": "Barkai",
           "email": "barkai@email.com", "password": "12345", "phone": "12345", "userStatus": 2}
my_user_list = [{"id": 10, "username": "Me", "firstName": "Noam", "lastName": "Barkai",
                 "email": "barkai@email.com", "password": "12345", "phone": "12345", "userStatus": 2},
                {"id": 11, "username": "theUser", "firstName": "John", "lastName": "James",
                 "email": "john@email.com", "password": "12345", "phone": "12345", "userStatus": 1}]


def test_put_pet():
    response = requests.put(f"{url}/pet", headers=header, data={'name': 'doge'})
    assert response.status_code == 200


def test_post_new_pet():
    response = requests.post(f"{url}/pet", headers=header, data=my_dog)
    assert response.status_code == 200


def test_get_pet_by_status():
    response = requests.get(f"{url}/pet/findByStatus", params="status=available", headers=header)
    json_data = json.loads(response.content)
    assert response.status_code == 200


def test_get_pet_by_tags():
    response = requests.get(f"{url}/pet/findByTags", params="tags=cat", headers=header)
    json_data = json.loads(response.content)
    assert response.status_code == 200


def test_get_pet_by_id():
    response = requests.get(f"{url}/pet/10", headers=header)
    json_data = json.loads(response.content)
    assert response.status_code == 200


def test_post_pet():
    response = requests.post(f"{url}/pet/11110", params="name=doge&status=available", headers=header)
    assert response.status_code == 200


def test_delete_pet():
    response = requests.delete(f"{url}/pet/2", headers=header)
    assert response.status_code == 200


def test_post_upload_image():
    response = requests.post(f"{url}/pet/11110/uploadImage", params="additionalMetadata=string", headers=header)
    assert response.status_code == 200


def test_get_inventory_by_status():
    response = requests.get(f"{url}/store/inventory", headers=header)
    json_data = json.loads(response.content)
    assert response.status_code == 200


def test_post_order():
    response = requests.post(f"{url}/store/order", params="petId:1", headers=header)
    assert response.status_code == 200


def test_get_order_by_id():
    response = requests.get(f"{url}/store/order/1", headers=header)
    json_data = json.loads(response.content)
    assert response.status_code == 200


def test_delete_order():
    response = requests.delete(f"{url}/store/order/1", headers=header)
    assert response.status_code == 200


def test_post_new_user():
    response = requests.post(f"{url}/user", headers=header, data=my_user)
    assert response.status_code == 200


def test_post_new_list_of_users():
    response = requests.post(f"{url}/user/createWithList", headers=header, data=my_user_list)
    assert response.status_code == 200


def test_get_user_into_system():
    response = requests.get(f"{url}/user/login", params="username=1&password=a", headers=header)
    assert response.status_code == 200


def test_get_user_out_of_system():
    response = requests.get(f"{url}/user/logout", headers=header)
    assert response.status_code == 200


def test_get_user_by_id():
    response = requests.get(f"{url}/user/a", headers=header)
    assert response.status_code == 200
