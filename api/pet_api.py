import requests
from models.Pet import Pet
from models.Pet import Status


class PetApi:

    def __init__(self, url="https://petstore3.swagger.io/api/v3"):
        self._url = url
        self._headers = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def put_pet(self, data: {str}) -> Pet:
        res = self._session.put(url=f"{self._url}/pet/", data=data, headers=self._headers)
        pet = res.json()
        if res.status_code == 200:
            my_pet = Pet(**pet)
            return my_pet
        else:
            return res.status_code

    def get_pet_by_id(self, pet_id: int) -> Pet:
        res = self._session.get(url=f"{self._url}/pet/{pet_id}", headers=self._headers)
        pet = res.json()

        if res.status_code == 200:
            my_pet = Pet(**pet)
            return my_pet
        else:
            return res.status_code

    def post_new_pet(self, pet) -> Pet:
        pet_data = pet.to_json()
        res = self._session.post(url=f"{self._url}/pet", data=pet_data, headers=self._headers)
        pet = res.json()
        if res.status_code == 200:
            my_pet = Pet(**pet)
            return my_pet
        else:
            return res.status_code

    def post_update_pet(self, param) -> Pet:
        res = self._session.post(url=f"{self._url}/pet/1", params=param, headers=self._headers)
        pet = res.json()
        if res.status_code == 200:
            my_pet = Pet(**pet)
            return my_pet
        else:
            return res.status_code

    def get_pet_by_status(self, status) -> [Pet]:
        res = self._session.get(url=f"{self._url}/pet/findByStatus?status={Status[status].value}",
                                headers=self._headers)
        pets = res.json()
        result = []
        if res.status_code == 200:
            for a in pets:
                pet = Pet(**a)
                result.append(pet)
            return result
        else:
            return res.status_code

    def get_pet_by_tags(self, tags: str) -> [Pet]:
        res = self._session.get(url=f"{self._url}/pet/findByTags", params=tags, headers=self._headers)
        pets = res.json()
        result = []
        if res.status_code == 200:
            for a in pets:
                pet = Pet(**a)
                result.append(pet)
            return result
        else:
            return res.status_code

    def delete_pet(self, id) -> Pet:
        res = self._session.delete(url=f"{self._url}/pet/{id}", headers=self._headers)
        if res.status_code == 200:
            res = self._session.get(url=f"{self._url}/pet/{id}", headers=self._headers)
            if res.status_code == 200:
                pet = res.json()
                my_pet = Pet(**pet)
                return my_pet
            else:
                return res.status_code

    def post_upload_image(self, image:str, id: int) -> Pet:
        res = self._session.delete(url=f"{self._url}/pet/{id}/uploadImage", params=image, headers=self._headers)
        if res.status_code == 200:
            pet = res.json()
            my_pet = Pet(**pet)
            return my_pet
        else:
            return res.status_code

