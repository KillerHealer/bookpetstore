

class Book:
    def __init__(self, isbn: str, title: str, subTitle: str, author: str,
                 publish_date: str, pages: int, description: str, website: str):
        self._isbn = isbn
        self._title = title
        self._subTitle = subTitle
        self._author = author
        self._publish_date = publish_date
        self._pages = pages
        self._description = description
        self._website = website

    @property
    def isbn(self):
        """
        gives back isbn
        :return: str
        """
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        """
        makes the isbn another one
        :param isbn: the isbn to be
        :return: str
        """
        self._isbn = isbn

    @property
    def title(self):
        """
        gives back title
        :return: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        makes the title another one
        :param title: the title to be
        :return: str
        """
        self._title = title

    @property
    def subTitle(self):
        """
        gives back subTitle
        :return: str
        """
        return self._subTitle

    @subTitle.setter
    def subTitle(self, subTitle):
        """
        makes the subTitle another one
        :param subTitle: the subTitle to be
        :return: str
        """
        self._subTitle = subTitle

    @property
    def author(self):
        """
        gives back author
        :return: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        makes the author another one
        :param author: the author to be
        :return: str
        """
        self._author = author

    @property
    def publish_date(self):
        """
        gives back publish_date
        :return: str
        """
        return self._publish_date

    @publish_date.setter
    def publish_date(self, publish_date):
        """
        makes the publish_date another one
        :param publish_date: the publish_date to be
        :return: str
        """
        self._publish_date = publish_date

    @property
    def pages(self):
        """
        gives back pages
        :return: str
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """
        makes the pages another one
        :param pages: the pages to be
        :return: str
        """
        self._pages = pages

    @property
    def description(self):
        """
        gives back description
        :return: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        makes the description another one
        :param description: the description to be
        :return: str
        """
        self._description = description

    @property
    def website(self):
        """
        gives back website
        :return: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """
        makes the website another one
        :param website: the website to be
        :return: str
        """
        self._website = website
