class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def borrow_book(self, book):
        if book.borrow_book():
            self.__borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.__borrowed_books and book.return_book():
            self.__borrowed_books.remove(book)
            return True
        return False

    def view_details(self):
        return f"Name: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {[book.get_title() for book in self.__borrowed_books]}"

    def __str__(self):
        return self.view_details()

    # Getters and setters for private attributes
    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    def set_name(self, name):
        self.__name = name

    def set_library_id(self, library_id):
        self.__library_id = library_id

    def set_borrowed_books(self, borrowed_books):
        self.__borrowed_books = borrowed_books
