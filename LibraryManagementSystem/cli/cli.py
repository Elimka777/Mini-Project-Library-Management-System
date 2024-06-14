from models.book import Book
from models.user import User
from models.author import Author
from models.genre import Genre
from utils.validation import validate_isbn, validate_date

class CLI:
    def __init__(self, library):
        self.library = library

    def main_menu(self):
        while True:
            print("Welcome to the Library Management System!")
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Genre Operations")
            print("5. Quit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.book_menu()
            elif choice == '2':
                self.user_menu()
            elif choice == '3':
                self.author_menu()
            elif choice == '4':
                self.genre_menu()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def book_menu(self):
        while True:
            print("Book Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.search_book()
            elif choice == '5':
                self.display_all_books()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        ISBN = input("Enter the book ISBN: ")
        genre = input("Enter the book genre: ")
        publication_date = input("Enter the publication date (YYYY-MM-DD): ")

        if not validate_isbn(ISBN):
            print("Invalid ISBN. Please try again.")
            return
        if not validate_date(publication_date):
            print("Invalid date format. Please try again.")
            return

        new_book = Book(title, author, ISBN, genre, publication_date)
        self.library.add_book(new_book)
        print("Book added successfully!")

    def borrow_book(self):
        ISBN = input("Enter the ISBN of the book to borrow: ")
        book = self.library.find_book(ISBN)
        if book:
            user_id = input("Enter your library ID: ")
            user = self.library.find_user(user_id)
            if user:
                if user.borrow_book(book):
                    print("Book borrowed successfully!")
                else:
                    print("Book is not available.")
            else:
                print("User not found.")
        else:
            print("Book not found.")

    def return_book(self):
        ISBN = input("Enter the ISBN of the book to return: ")
        book = self.library.find_book(ISBN)
        if book:
            user_id = input("Enter your library ID: ")
            user = self.library.find_user(user_id)
            if user:
                if user.return_book(book):
                    print("Book returned successfully!")
                else:
                    print("Book was not borrowed by you.")
            else:
                print("User not found.")
        else:
            print("Book not found.")

    def search_book(self):
        ISBN = input("Enter the ISBN of the book to search for: ")
        book = self.library.find_book(ISBN)
        if book:
            print(book)
        else:
            print("Book not found.")

    def display_all_books(self):
        books = self.library.display_all_books()
        if books:
            for book in books:
                print(book)
        else:
            print("No books available.")

    def user_menu(self):
        while True:
            print("User Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.view_user_details()
            elif choice == '3':
                self.display_all_users()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def add_user(self):
        name = input("Enter the user name: ")
        library_id = input("Enter the user library ID: ")
        new_user = User(name, library_id)
        self.library.add_user(new_user)
        print("User added successfully!")

    def view_user_details(self):
        library_id = input("Enter the library ID of the user: ")
        user = self.library.find_user(library_id)
        if user:
            print(user)
        else:
            print("User not found.")

    def display_all_users(self):
        users = self.library.display_all_users()
        if users:
            for user in users:
                print(user)
        else:
            print("No users available.")

    def author_menu(self):
        while True:
            print("Author Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_author()
            elif choice == '2':
                self.view_author_details()
            elif choice == '3':
                self.display_all_authors()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def add_author(self):
        name = input("Enter the author name: ")
        biography = input("Enter the author biography: ")
        new_author = Author(name, biography)
        self.library.add_author(new_author)
        print("Author added successfully!")

    def view_author_details(self):
        name = input("Enter the author name: ")
        author = self.library.find_author(name)
        if author:
            print(author)
        else:
            print("Author not found.")

    def display_all_authors(self):
        authors = self.library.display_all_authors()
        if authors:
            for author in authors:
                print(author)
        else:
            print("No authors available.")

    def genre_menu(self):
        while True:
            print("Genre Operations:")
            print("1. Add a new genre")
            print("2. View genre details")
            print("3. Display all genres")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_genre()
            elif choice == '2':
                self.view_genre_details()
            elif choice == '3':
                self.display_all_genres()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def add_genre(self):
        name = input("Enter the genre name: ")
        description = input("Enter the genre description: ")
        category = input("Enter the genre category: ")
        new_genre = Genre(name, description, category)
        self.library.add_genre(new_genre)
        print("Genre added successfully!")

    def view_genre_details(self):
        name = input("Enter the genre name: ")
        genre = self.library.find_genre(name)
        if genre:
            print(genre)
        else:
            print("Genre not found.")

    def display_all_genres(self):
        genres = self.library.display_all_genres()
        if genres:
            for genre in genres:
                print(genre)
        else:
            print("No genres available.")
