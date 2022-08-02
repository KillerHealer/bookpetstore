import requests
from models.Pet import Pet
from models.Pet import Status


class PetApi:

    def __init__(self, url="https://petstore3.swagger.io/api/v3"):
        self._url = url
        self._headers = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def get_pet_by_id(self, pet_id: int) -> Pet:
        res = self._session.get(url=f"{self._url}/pet/{pet_id}")
        pet = res.json()

        if res.status_code == 200:
            my_pet = Pet(**pet)
            return my_pet
        else:
            return None

    def post_new_pet(self, pet) -> Pet:
        pet_data = pet.to_json()
        res = self._session.post(url=f"{self._url}/pet", data=pet_data)
        pet = res.json()
        if res.status_code == 200:
            my_pet = Pet(**pet)
            return my_pet
        else:
            return None

    def get_pet_by_status(self, status) -> [Pet]:
        res = self._session.get(url=f"{self._url}/pet/findByStatus?status={Status[status].value}")
        pets = res.json()
        result = []
        for a in pets:
            pet = Pet(**a)
            result.append(pet)
        return result
