from models.book import Book
from models.user import User
from models.author import Author
from models.genre import Genre

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.genres = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, ISBN):
        self.books = [book for book in self.books if book.get_ISBN() != ISBN]

    def add_user(self, user):
        self.users.append(user)

    def add_author(self, author):
        self.authors.append(author)

    def add_genre(self, genre):
        self.genres.append(genre)

    def find_book(self, ISBN):
        for book in self.books:
            if book.get_ISBN() == ISBN:
                return book
        return None

    def find_user(self, library_id):
        for user in self.users:
            if user.get_library_id() == library_id:
                return user
        return None

    def find_author(self, name):
        for author in self.authors:
            if author.get_name() == name:
                return author
        return None

    def find_genre(self, name):
        for genre in self.genres:
            if genre.get_name() == name:
                return genre
        return None

    def display_all_books(self):
        return [str(book) for book in self.books]

    def display_all_users(self):
        return [str(user) for user in self.users]

    def display_all_authors(self):
        return [str(author) for author in self.authors]

    def display_all_genres(self):
        return [str(genre) for genre in self.genres]
