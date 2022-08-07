import pytest
import logging
import requests
from api import pet_api
from api import order_api
from api.order_api import Inventory
from models import Pet
from models.Pet import Status
from models.order import Order, OrderStatus

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
my_order = Order(1, 19872, 5, "2022-08-06T23:31:28.815+00:00", OrderStatus.approved, False)
apiP = pet_api.PetApi()
apiO = order_api.OrderApi()


@pytest.mark.pet()
def test_put_pet():
    """
    tries to update the name of the pet
    :return:
    """
    logging.info("trying to find and update the pet")
    response = apiP.put_pet({'name': 'doge'})
    if isinstance(response, Pet.Pet):
        assert response.name == "doge"
    else:
        logging.warning(f"status code {response} from put pet")
        assert False


@pytest.mark.pet()
def test_post_new_pet():
    """
    tries to add a new pet to the system
    :return:
    """
    logging.info("trying to add a new pet")
    response = apiP.post_new_pet(my_dog)
    if isinstance(response, Pet.Pet):
        assert response.id == my_dog.id
    else:
        logging.warning(f"status code {response} from post new pet")
        assert False


@pytest.mark.pet()
def test_get_pet_by_status():
    """
    tries to find all the pets that have the status given
    :return:
    """
    logging.info("trying to find all pets with the status")
    response = apiP.get_pet_by_status("available")
    if isinstance(response, (list, Pet.Pet)):
        for res in response:
            if res.status != Status.available.name:
                assert False
        assert True
    else:
        logging.warning(f"status code {response} from get pet by status")
        assert False


@pytest.mark.pet()
def test_get_pet_by_tags():
    """
    tries to find all pets with the given tags
    :return:
    """
    logging.info("trying to find pets with given tags")
    response = apiP.get_pet_by_tags("tags=cat")
    if isinstance(response, (list, Pet.Pet)):
        for res in response:
            if res.tags != "cat":
                assert False
        assert True
    else:
        logging.warning(f"status code {response} from get pet by tags")
        assert False


@pytest.mark.pet()
def test_get_pet_by_id():
    """
    tries to find all pets with given id
    :return:
    """
    logging.info("trying to find pets with given id")
    response = apiP.get_pet_by_id(10)
    if isinstance(response, Pet.Pet):
        assert response.id == 10
    else:
        logging.warning(f"status code {response} from get pet by id")
        assert False


@pytest.mark.pet()
def test_post_pet():
    """
    finds pet by id and updates name and status
    :return:
    """
    logging.info("finding pet by id and updating name and status")
    response = apiP.post_update_pet("name=doge&status=available")
    if isinstance(response, Pet.Pet):
        assert response.name == "doge"
    else:
        logging.warning(f"status code {response} from update pet name")
        assert False


@pytest.mark.pet()
def test_delete_pet():
    """
    finds pet by id and deletes it
    :return:
    """
    logging.info("finding pet by id and deleting it")
    response = apiP.delete_pet(2)
    if isinstance(response, Pet.Pet):
        logging.warning(f"couldn't delete pet for some reason")
        assert False
    else:
        logging.warning(f"didn't find the deleted pet, good.")
        assert True


@pytest.mark.pet()
def test_post_upload_image():
    """
    finds pet with id and uploads an image for it
    :return:
    """
    logging.info("finding pet by id and uploads an image for it")
    response = apiP.post_upload_image("additionalMetadata=string", 11110)
    if isinstance(response, Pet.Pet):
        assert response.photourls == "string"
    else:
        logging.warning(f"status code {response} from upload image")
        assert False


@pytest.mark.store()
def test_get_inventory_by_status():
    """
    finds the number of approved, placed and delivered pets in inventory
    :return:
    """
    logging.info("finding inventory")
    response = apiO.get_inventory()
    if isinstance(response, Inventory):
        assert True
    else:
        logging.warning(f"status code {response} from get inventory")
        assert False


@pytest.mark.store()
def test_post_order():
    """
     makes a new order for a pet/s
    :return:
    """
    logging.info("making an order for it")
    response = apiO.post_new_order(my_order)
    if isinstance(response, Order):
        assert response.id == my_order.id
    else:
        logging.warning(f"status code {response} from post new order")


@pytest.mark.store()
def test_get_order_by_id():
    """
    finds order by id
    :return:
    """
    logging.info("finding order by id")
    response = apiO.get_order_by_id(1)
    if isinstance(response, Order):
        assert response.id == 1
    else:
        logging.warning(f"status code {response} from get order")


@pytest.mark.store()
def test_delete_order():
    """
    finds order by id and deletes it
    :return:
    """
    logging.info("finding order by id and deleting it")
    response = apiO.delete_order_by_id(1)
    if isinstance(response, Order):
        logging.warning(f"couldn't delete order for some reason")
        assert False
    else:
        logging.warning(f"didn't find the deleted pet, good.")
        assert True


@pytest.mark.user()
def test_post_new_user():
    """
    creates a new user and adds it to the system
    :return:
    """
    logging.info("creating new user and adding it to the system")
    response = requests.post(f"{url}/user", headers=header, data=my_user)
    assert response.status_code == 200


@pytest.mark.user()
def test_post_new_list_of_users():
    """
    creates new users from the list and adds them to the system
    :return:
    """
    logging.info("creating new users and adding them to the system")
    response = requests.post(f"{url}/user/createWithList", headers=header, data=my_user_list)
    assert response.status_code == 200


@pytest.mark.user()
def test_get_user_into_system():
    """
    logs in the user to the system with username and password
    :return:
    """
    logging.info("logging in user")
    response = requests.get(f"{url}/user/login", params="username=1&password=a", headers=header)
    assert response.status_code == 200


@pytest.mark.user()
def test_get_user_out_of_system():
    """
    logs user out of the system
    :return:
    """
    logging.info("logging the current user out of the system")
    response = requests.get(f"{url}/user/logout", headers=header)
    assert response.status_code == 200


@pytest.mark.user()
def test_get_user_by_id():
    """
    finds user by id
    :return:
    """
    logging.info("finding user by id")
    response = requests.get(f"{url}/user/a", headers=header)
    assert response.status_code == 200


@pytest.mark.user()
def test_put_logged_in_user():
    """
    updates an existent user in the store
    :return:
    """
    response = requests.get(f"{url}/user/theUser", headers=header)
    assert response.status_code == 200


@pytest.mark.user()
def test_delete_user():
    """
    finds user by name and deletes it
    :return:
    """
    logging.info("finding user by id and deletes it")
    response = requests.delete(f"{url}/user/theUser", headers=header)
    assert response.status_code == 200
