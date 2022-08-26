import pytest
import logging
import requests
from api import pet_api
from api import order_api
from api.order_api import Inventory
from api.user_api import UserApi
from models.user import User
from models import Pet
from models.Pet import Status
from models.order import Order, OrderStatus

files = 'doggy.jpg'
url = "https://petstore3.swagger.io/api/v3"
header = {'accept': 'application/json'}
dog_category = {"id": 1, "name": "Dogs"}
my_dog = Pet.Pet(11110, "my_dog", dog_category, "available")
my_user = User(10, "Me", "Noam", "Barkai", "barkai@email.com", "12345", "12345", 2)
my_user1 = User(11, "you", "Mishel", "Barkai", "barkai23@email.com", "12332", "12344", 3)
my_user_list = [{"id": 12,
                 "username": "User",
                 "firstName": "John",
                 "lastName": "James",
                 "email": "john@email.com",
                 "password": "12345",
                 "phone": "12345",
                 "userStatus": 1}]
my_order = Order(1, 19872, 5, "2022-08-06T23:31:28.815+00:00", OrderStatus.approved, False)
apiP = pet_api.PetApi()
apiO = order_api.OrderApi()
apiU = UserApi()


@pytest.mark.pet()
def test_put_pet(params):
    """
    tries to update the name of the pet
    :return:
    """
    logging.info("trying to find and update the pet")
    new_pet = apiP.put_pet({'name': 'doge'}, params["URL"])
    assert new_pet.name == "doge"
    # logging.warning(f"status code {response} from put pet")


@pytest.mark.pet()
def test_post_new_pet(params):
    """
    tries to add a new pet to the system
    :return:
    """
    logging.info("trying to add a new pet")
    new_pet = apiP.post_new_pet(my_dog, params["URL"])
    assert new_pet.id == my_dog.id
    # logging.warning(f"status code {response} from post new pet")


@pytest.mark.pet()
def test_get_pet_by_status(params):
    """
    tries to find all the pets that have the status given
    :return:
    """
    logging.info("trying to find all pets with the status")
    pet_list = apiP.get_pet_by_status("available", params["URL"])
    for pet in pet_list:
        if pet.status != Status.available.name:
            assert False
    assert True
    # logging.warning(f"status code {response} from get pet by status")


@pytest.mark.pet()
def test_get_pet_by_tags(params):
    """
    tries to find all pets with the given tags
    :return:
    """
    logging.info("trying to find pets with given tags")
    pet_list = apiP.get_pet_by_tags("tags=cat", params["URL"])
    for pet in pet_list:
        if pet.tags != "cat":
            assert False
    assert True
    # logging.warning(f"status code {response} from get pet by tags")


@pytest.mark.pet()
def test_get_pet_by_id(params):
    """
    tries to find all pets with given id
    :return:
    """
    logging.info("trying to find pets with given id")
    pet_with_id = apiP.get_pet_by_id(10, params["URL"])
    assert pet_with_id.id == 10
    # logging.warning(f"status code {response} from get pet by id")


@pytest.mark.pet()
def test_post_pet(params):
    """
    finds pet by id and updates name and status
    :return:
    """
    logging.info("finding pet by id and updating name and status")
    updated_pet = apiP.post_update_pet("name=doge&status=available", params["URL"])
    assert updated_pet.name == "doge"
    # logging.warning(f"status code {response} from update pet name")


@pytest.mark.pet()
def test_delete_pet(params):
    """
    finds pet by id deletes it and then tries to find it again
    :return:
    """
    logging.info("finding pet by id and deleting it")
    deleted_pet = apiP.delete_pet(2, params["URL"])
    if isinstance(deleted_pet, Pet.Pet):
        logging.warning(f"couldn't delete pet for some reason")
        assert False
    else:
        logging.warning(f"didn't find the deleted pet, good.")
        assert True


@pytest.mark.pet()
def test_post_upload_image(params):
    """
    finds pet with id and uploads an image for it
    :return:
    """
    pet = apiP.post_new_pet(my_dog)
    logging.info("finding pet by id and uploads an image for it")
    pet_with_image = apiP.post_upload_image("additionalMetadata=string", pet.id, files, params["URL"])
    logging.warning(f"{pet_with_image}")
    assert pet_with_image.photourls == files
    # logging.warning(f"status code {response} from upload image")


@pytest.mark.store()
def test_get_inventory_by_status(params):
    """
    finds the number of approved, placed and delivered pets in inventory
    :return:
    """
    logging.info("finding inventory")
    new_inventory = apiO.get_inventory(params["URL"])
    assert isinstance(new_inventory, Inventory)
    # logging.warning(f"status code {response} from get inventory")


@pytest.mark.store()
def test_post_order(params):
    """
     makes a new order for a pet/s
    :return:
    """
    logging.info("making an order for it")
    new_order = apiO.post_new_order(my_order, params["URL"])
    assert new_order.id == my_order.id
    # logging.warning(f"status code {response} from post new order")


@pytest.mark.store()
def test_get_order_by_id(params):
    """
    finds order by id
    :return:
    """
    logging.info("finding order by id")
    response = apiO.get_order_by_id(1, params["URL"])
    assert response.id == 1
    # logging.warning(f"status code {response} from get order")


@pytest.mark.store()
def test_delete_order(params):
    """
    finds order by id deletes it and then tries to find it again
    :return:
    """
    logging.info("finding order by id and deleting it")
    deleted_order = apiO.delete_order_by_id(1, params["URL"])
    if isinstance(deleted_order, Order):
        logging.warning(f"couldn't delete order for some reason")
        assert False
    else:
        logging.warning(f"didn't find the deleted pet, good.")
        assert True


@pytest.mark.user()
def test_post_new_user(params):
    """
    creates a new user and adds it to the system
    :return:
    """
    logging.info("creating new user and adding it to the system")
    new_user = apiU.post_new_user(my_user, params["URL"])
    assert new_user.id == my_user.id
    # logging.warning(f"status code {response} from post new user")


@pytest.mark.user()
def test_post_new_list_of_users(params):
    """
    creates new users from the list and adds them to the system
    :return:
    """
    logging.info("creating new users and adding them to the system")
    user_list = apiU.post_list_of_new_users(my_user_list.__str__(), params["URL"])
    assert len(user_list) == len(my_user_list)
    # logging.warning(f"status code {response} from post new user list")


@pytest.mark.user()
def test_get_user_into_system(params):
    """
    logs in the user to the system with username and password
    :return:
    """
    logging.info("logging in user")
    login_info = apiU.get_user_logged_in("username=1&password=a", params["URL"])
    if isinstance(login_info, str):
        logging.warning(f"{login_info} success")
        assert True
    else:
        logging.warning(f"status code {login_info} from get user logged in")
        assert False


@pytest.mark.user()
def test_get_user_out_of_system(params):
    """
    logs user out of the system
    :return:
    """
    logging.info("logging the current user out of the system")
    logout_info = apiU.get_user_logged_out(params["URL"])
    if isinstance(logout_info, str):
        logging.warning(f"{logout_info} success")
        assert True
    else:
        logging.warning(f"status code {logout_info} from get user logged in")
        assert False


@pytest.mark.user()
def test_get_user_by_username(params):
    """
    finds user by username
    :return:
    """
    logging.info("finding user by username")
    user_with_username = apiU.get_user_by_username("Me", params["URL"])
    assert user_with_username.id == my_user.id
    # logging.warning(f"status code {response} from get user by id")


@pytest.mark.user()
def test_put_update_user(params):
    """
    updates an existent user to a default state in the store
    :return:
    """
    updated_user = apiU.put_update_user("a", params["URL"])
    assert updated_user.id == my_user.id
    # logging.warning(f"status code {response} from get user by id")


@pytest.mark.user()
def test_delete_user(params):
    """
    finds user by name and deletes it
    :return:
    """
    logging.info("finding user by id and deletes it")
    deleted_user = apiU.delete_user("a", params["URL"])
    if isinstance(deleted_user, User):
        logging.warning("couldn't delete user")
        assert False
    else:
        logging.warning(f"status code {deleted_user} from delete user which means success!")
        assert True
