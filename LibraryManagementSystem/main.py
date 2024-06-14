from cli.cli import CLI
from models.library import Library

def main():
    library = Library()
    cli = CLI(library)
    cli.main_menu()

if __name__ == "__main__":
    main()
