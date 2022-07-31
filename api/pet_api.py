import requests
from models.Pet import Pet
from models.Pet import Status


class petApi:

    def __init__(self, url="https://petstore3.swagger.io/api/v3"):
        self.url = url
        self.headrs = {'accept': 'application/json'}
        self.session = requests.session()
        self.session.headers.update(self.headrs)

    def get_pet_by_id(self,pet_id : int)->Pet:
        res = self.session.get(url=f"{self.url}/pet/{pet_id}")
        pet = res.json()

        if res.status_code == 200:
            my_pet = Pet(**pet)
            return my_pet
        else:
            return None


    def post_new_pet(self,pet )->Pet:
        pet_data = pet.to_json()
        res = self.session.post(url=f"{self.url}/pet", data=pet_data)
        pet = res.json()
        if res.status_code == 200:
            my_pet = Pet(**pet)
            return my_pet
        else:
            return None

    def get_pet_by_status(self, status) -> [Pet]:
        res = self.session.get(url=f"{self.url}/pet/findByStatus?status={Status[status].value}")
        pets = res.json()
        result = []
        for a in pets:
            pet = Pet(**a)
            result.append(pet)
        return result
