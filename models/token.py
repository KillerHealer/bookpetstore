
class Token:
    def __init__(self, token: str, expires: str, status: str, result: str):
        self._token = token
        self._expires = expires
        self._status = status
        self._result = result

