class Book:
    def __init__(self, title, author, ISBN, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__ISBN = ISBN
        self.__genre = genre
        self.__publication_date = publication_date
        self.__availability_status = "Available"

    def borrow_book(self):
        if self.__availability_status == "Available":
            self.__availability_status = "Borrowed"
            return True
        return False

    def return_book(self):
        if self.__availability_status == "Borrowed":
            self.__availability_status = "Available"
            return True
        return False

    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__ISBN}, Genre: {self.__genre}, Published: {self.__publication_date}, Status: {self.__availability_status}"

    # Getters and setters for private attributes
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_ISBN(self):
        return self.__ISBN

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date

    def get_availability_status(self):
        return self.__availability_status

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_ISBN(self, ISBN):
        self.__ISBN = ISBN

    def set_genre(self, genre):
        self.__genre = genre

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    def set_availability_status(self, status):
        self.__availability_status = status
