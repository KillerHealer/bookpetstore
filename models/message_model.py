

class MessageModel:
    def __init__(self, code: int, message: str):
        self._code = code
        self._message = message

    @property
    def code(self):
        """
        gives back code
        :return: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        makes the code another one
        :param code: the code to be
        :return: int
        """
        self._code = code

    @property
    def message(self):
        """
        gives back message
        :return: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        makes the message another one
        :param message: the message to be
        :return: str
        """
        self._message = message
