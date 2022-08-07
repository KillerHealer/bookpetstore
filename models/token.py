
class Token:
    def __init__(self, token: str, expires: str, status: str, result: str):
        self._token = token
        self._expires = expires
        self._status = status
        self._result = result

    @property
    def token(self):
        """
        gives back token
        :return: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        makes the token another one
        :param token: the token to be
        :return: str
        """
        self._token = token
