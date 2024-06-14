class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def view_details(self):
        return f"Name: {self.__name}, Biography: {self.__biography}"

    def __str__(self):
        return self.view_details()

    # Getters and setters for private attributes
    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

    def set_name(self, name):
        self.__name = name

    def set_biography(self, biography):
        self.__biography = biography
