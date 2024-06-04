class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        if not 5 <= len(value) <= 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = value

    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError("Can't modify existing attributes")
        super().__setattr__(name, value)
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not name:
            raise ValueError("Name must not be empty")
        self._name = name

    @property
    def name(self):
        return self._name

    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError("Can't modify existing attributes")
        super().__setattr__(name, value)

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 2 <= len(value) <= 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        if not value:
            raise ValueError("Category must not be empty")
        self._category = value

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass