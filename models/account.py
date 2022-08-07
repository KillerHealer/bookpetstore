from models.book import Book


class Account:
    def __init__(self, userID: str, username: str, books: Book):
        self._userID = userID
        self._username = username
        self._books = books

    @property
    def userID(self):
        """
        gives back userId
        :return: str
        """
        return self._userID

    @userID.setter
    def userID(self, userID):
        """
        makes the userId another one
        :param userID: the userId to be
        :return: str
        """
        self._userID = userID

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
