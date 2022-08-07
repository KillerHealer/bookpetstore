from models.book import Book


class Account:
    def __init__(self, userId: str, username: str, books: Book):
        self._userId = userId
        self._username = username
        self._books = books

    @property
    def userId(self):
        """
        gives back userId
        :return: str
        """
        return self._userId

    @userId.setter
    def userId(self, userId):
        """
        makes the userId another one
        :param userId: the userId to be
        :return: str
        """
        self._userId = userId

    @property
    def username(self):
        """
        gives back username
        :return: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        makes the username another one
        :param username: the username to be
        :return: str
        """
        self._username = username
