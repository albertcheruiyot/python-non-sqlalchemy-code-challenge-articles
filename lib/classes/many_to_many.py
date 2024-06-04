class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if not name or len(name) == 0:
            raise ValueError("Name must have at least one character.")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all_articles() if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        return list(set(article.magazine.category for article in self.articles()))

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters.")
        self._name = name
        
        if not isinstance(category, str):
            raise ValueError("Category must be a string.")
        if not category or len(category) == 0:
            raise ValueError("Category must have at least one character.")
        self._category = category

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return [article for article in Article.all_articles() if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        return list(set(article.author for article in self.articles()))

class Article:
    _all_articles = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters.")
        self._title = title
        self.author = author
        self.magazine = magazine
        Article._all_articles.append(self)

    @classmethod
    def all_articles(cls):
        return cls._all_articles

    @property
    def title(self):
        return self._title


'''class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        self.name = name

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

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass'''

        