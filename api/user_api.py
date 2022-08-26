import json

import requests
from models.user import User


class UserApi:
    def __init__(self, url: str = "https://petstore3.swagger.io/api/v3/user"):
        self._url = url
        self._headers = {'accept': 'application/json'}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def post_new_user(self, my_user, url: str = "https://petstore3.swagger.io/api/v3/user") -> User or int:
        my_user_data = my_user.to_json()
        res = self._session.post(url=f"{url}", data=my_user_data, headers=self._headers)
        if res.status_code == 200:
            u1 = User(**res.json())
            return u1
        else:
            return res.status_code

    def post_list_of_new_users(self, user_list: [User], url: str = "https://petstore3.swagger.io/api/v3/user") -> [User] or int:
        #user_list_data = []
        #for user in user_list:
            #for u in user:
                #user_list_data.append(u.to_json())
        ulist = []
        res = self._session.post(url=f"{url}/createWithList", data=user_list, headers=self._headers)
        if res.status_code == 200:
            for user in res:
                u1 = User(**user.json())
                ulist.append(u1)
                return ulist
        else:
            return res.status_code

    def get_user_logged_in(self, usepass: str, url: str = "https://petstore3.swagger.io/api/v3/user") -> str or int:
        res = self._session.get(f"{url}/login", params=usepass, headers=self._headers)
        if res.status_code == 200:
            return res.content.__str__()
        else:
            return res.status_code

    def get_user_logged_out(self, url: str = "https://petstore3.swagger.io/api/v3/user") -> str or int:
        res = self._session.get(f"{url}/logout", headers=self._headers)
        if res.status_code == 200:
            return res.content.__str__()
        else:
            return res.status_code

    def get_user_by_username(self, username, url: str = "https://petstore3.swagger.io/api/v3/user") -> User or int:
        res = self._session.get(f"{url}/{username}", headers=self._headers)
        if res.status_code == 200:
            u1 = User(**res.json())
            return u1
        else:
            return res.status_code

    def put_update_user(self, username: str, url: str = "https://petstore3.swagger.io/api/v3/user") -> User or int:
        res = self._session.put(f"{url}/{username}", headers=self._headers)
        if res.status_code == 200:
            u1 = User(**res.json())
            return u1
        else:
            return res.status_code

    def delete_user(self, username: str, url: str = "https://petstore3.swagger.io/api/v3/user") -> User or int:
        res = self._session.delete(f"{url}/{username}", headers=self._headers)
        if res.status_code == 200:
            res = self._session.get(f"{url}/{username}", headers=self._headers)
            if res.status_code == 200:
                u1 = User(**res.json())
                return u1
            else:
                return res.status_code
