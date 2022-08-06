import pytest
import logging
import requests
from api import pet_api
from models import Pet
from models.Pet import Status

url = "https://petstore3.swagger.io/api/v3"
header = {'accept': 'application/json'}
dog_category = {"id": 1, "name": "Dogs"}
my_dog = Pet.Pet(1, "my_dog", dog_category, "available")
my_user = {"id": 10, "username": "Me", "firstName": "Noam", "lastName": "Barkai",
           "email": "barkai@email.com", "password": "12345", "phone": "12345", "userStatus": 2}
my_user_list = """[{"id": 10, "username": "Me", "firstName": "Noam", "lastName": "Barkai",
                 "email": "barkai@email.com", "password": "12345", "phone": "12345", "userStatus": 2},
                {"id": 11, "username": "theUser", "firstName": "John", "lastName": "James",
                 "email": "john@email.com", "password": "12345", "phone": "12345", "userStatus": 1}]"""
api = pet_api.PetApi()


def test_put_pet():
    """
    tries to update the name of the pet
    :return:
    """
    logging.info("trying to find and update the pet")
    response = api.put_pet({'name': 'doge'})
    if type(response) == Pet:
        assert response.name == "doge"
    else:
        logging.warning(f"status code {response}")
        assert False


def test_post_new_pet():
    """
    tries to add a new pet to the system
    :return:
    """
    logging.info("trying to add a new pet")
    response = api.post_new_pet(my_dog)
    if type(response) == Pet:
        assert response.id == my_dog.id
    else:
        logging.warning(f"status code {response}")
        assert False


def test_get_pet_by_status():
    """
    tries to find all the pets that have the status given
    :return:
    """
    logging.info("trying to find all pets with the status")
    response = api.get_pet_by_status("available")
    if type(response) == [Pet]:
        for res in response:
            if res.status != Status.available:
                assert False
        assert True
    else:
        logging.warning(f"status code {response}")
        assert False


def test_get_pet_by_tags():
    """
    tries to find all pets with the given tags
    :return:
    """
    logging.info("trying to find pets with given tags")
    response = api.get_pet_by_tags("tags=cat")
    if isinstance(response, (list,Pet.Pet)):
        for res in response:
            if res.tags != Status.available:
                assert False
        assert True
    else:
        logging.warning(f"status code {response}")
        assert False


def test_get_pet_by_id():
    """
    tries to find all pets with given id
    :return:
    """
    logging.info("trying to find pets with given id")
    response = api.get_pet_by_id(10)
    if isinstance(response, Pet.Pet):
        assert response.id == 10
    else:
        logging.warning(f"status code {response}")
        assert False


def test_post_pet():
    """
    finds pet by id and updates name and status
    :return:
    """
    logging.info("finding pet by id and updating name and status")
    response = api.post_update_pet("name=doge&status=available")
    if type(response) == Pet:
        assert response.name == "doge"
    else:
        logging.warning(f"status code {response}")
        assert False


def test_delete_pet():
    """
    finds pet by id and deletes it
    :return:
    """
    logging.info("finding pet by id and deleting it")
    response = api.delete_pet(2)
    if type(response) == Pet:
        assert False
    else:
        logging.warning(f"didn't find the deleted pet good: {response}")
        assert False


def test_post_upload_image():
    """
    finds pet with id and uploads an image for it
    :return:
    """
    logging.info("finding pet by id and uploads an image for it")
    response = api.post_upload_image("additionalMetadata=string", 11110)
    if type(response) == Pet:
        assert response.photourls == "string"
    else:
        logging.warning(f"status code {response}")
        assert False


def test_get_inventory_by_status():
    """
    finds the number of approved, placed and delivered pets in inventory
    :return:
    """
    logging.info("finding inventory")
    response = requests.get(f"{url}/store/inventory", headers=header)
    assert response.status_code == 200


def test_post_order():
    """
    finds pet by id and sets an order for it
    :return:
    """
    logging.info("finding pet by id and setting an order for it")
    response = requests.post(f"{url}/store/order", params="petId:1", headers=header)
    assert response.status_code == 200


def test_get_order_by_id():
    """
    finds order by id
    :return:
    """
    logging.info("finding order by id")
    response = requests.get(f"{url}/store/order/1", headers=header)
    assert response.status_code == 200


def test_delete_order():
    """
    finds order by id and deletes it
    :return:
    """
    logging.info("finding order by id and deleting it")
    response = requests.delete(f"{url}/store/order/1", headers=header)
    assert response.status_code == 200


def test_post_new_user():
    """
    creates a new user and adds it to the system
    :return:
    """
    logging.info("creating new user and adding it to the system")
    response = requests.post(f"{url}/user", headers=header, data=my_user)
    assert response.status_code == 200


def test_post_new_list_of_users():
    """
    creates new users from the list and adds them to the system
    :return:
    """
    logging.info("creating new users and adding them to the system")
    response = requests.post(f"{url}/user/createWithList", headers=header, data=my_user_list)
    assert response.status_code == 200


def test_get_user_into_system():
    """
    logs in the user to the system with username and password
    :return:
    """
    logging.info("logging in user")
    response = requests.get(f"{url}/user/login", params="username=1&password=a", headers=header)
    assert response.status_code == 200


def test_get_user_out_of_system():
    """
    logs user out of the system
    :return:
    """
    logging.info("logging the current user out of the system")
    response = requests.get(f"{url}/user/logout", headers=header)
    assert response.status_code == 200


def test_get_user_by_id():
    """
    finds user by id
    :return:
    """
    logging.info("finding user by id")
    response = requests.get(f"{url}/user/a", headers=header)
    assert response.status_code == 200


def test_put_logged_in_user():
    """
    updates an existent user in the store
    :return:
    """
    response = requests.get(f"{url}/user/theUser", headers=header)
    assert response.status_code == 200


def test_delete_user():
    """
    finds user by name and deletes it
    :return:
    """
    logging.info("finding user by id and deletes it")
    response = requests.delete(f"{url}/user/theUser", headers=header)
    assert response.status_code == 200
