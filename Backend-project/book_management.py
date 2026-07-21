# Book Management System (OOP) Console Application
# Demonstrates: classes, encapsulation, inheritance, polymorphism,
# variables, conditionals, loops, lists, functions, file operations, validation

BOOKS_FILE = "books.txt"


class Book:
    # Base class representing a single book
    def __init__(self, title, author, year):
        # Encapsulation: attributes are private (double underscore)
        self.__title = title
        self.__author = author
        self.__year = year

    # Getter methods: controlled access to private attributes (encapsulation)
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    # Setter methods: controlled modification with validation (encapsulation)
    def set_title(self, new_title):
        # Validation: title must not be empty
        if isinstance(new_title, str) and new_title.strip() != "":
            self.__title = new_title
        else:
            print("Invalid title! Title cannot be empty.")

    def set_author(self, new_author):
        # Validation: author must not be empty
        if isinstance(new_author, str) and new_author.strip() != "":
            self.__author = new_author
        else:
            print("Invalid author! Author cannot be empty.")

    def set_year(self, new_year):
        # Validation: year must be a positive integer
        if isinstance(new_year, int) and new_year > 0:
            self.__year = new_year
        else:
            print("Invalid year! Year must be a positive integer.")

    def display_info(self):
        # Polymorphism: subclasses override this method with their own version
        return f"'{self.__title}' by {self.__author} ({self.__year})"

    def to_file_line(self):
        # Convert book data to a single text line for saving to file
        return f"{self.__title};{self.__author};{self.__year}"


class EBook(Book):
    # Inheritance: EBook extends Book with an extra attribute
    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)  # call parent constructor
        self.__file_size_mb = file_size_mb

    def display_info(self):
        # Polymorphism: same method name, different behavior than Book
        base_info = super().display_info()
        return f"{base_info} [E-Book, {self.__file_size_mb} MB]"


class BookManager:
    # Manager class responsible for the list of books
    def __init__(self):
        self.__books = []  # encapsulated list of Book objects

    def add_book(self, book):
        # Add a new Book (or EBook) object to the list
        self.__books.append(book)
        print("Book added successfully.")

    def show_all_books(self):
        # Display all books using a loop.
        # Polymorphism in action: display_info() behaves differently
        # for Book and EBook objects in the same list.
        if not self.__books:
            print("No books in the list.")
            return
        for i, book in enumerate(self.__books, start=1):
            print(f"{i}. {book.display_info()}")

    def search_by_title(self, title):
        # Search for books whose title contains the given text
        found = False
        for book in self.__books:
            if title.lower() in book.get_title().lower():
                print("Found:", book.display_info())
                found = True
        if not found:
            print("No book found with that title.")

    def save_to_file(self):
        # Write all books to the text file (file creation/editing)
        with open(BOOKS_FILE, "w", encoding="utf-8") as file:
            for book in self.__books:
                file.write(book.to_file_line() + "\n")
        print("Books saved to file.")

    def load_from_file(self):
        # Read books from the text file if it exists
        try:
            with open(BOOKS_FILE, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(";")
                    if len(parts) == 3:
                        title, author, year = parts
                        self.__books.append(Book(title, author, int(year)))
            print("Books loaded from file.")
        except FileNotFoundError:
            print("No saved file found, starting with an empty list.")

    def clear_file(self):
        # Delete all saved data from the file (file deleting skill)
        open(BOOKS_FILE, "w").close()
        self.__books = []
        print("All books and file data cleared.")


def get_valid_number(prompt):
    # Validation: input must be a positive whole number
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        print("Invalid input! Please enter a number.")


def add_book_menu(manager):
    # Collect book data from the user with validation, then add it
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()

    # Validation: title and author must not be empty
    if not title or not author:
        print("Title and author cannot be empty!")
        return

    year = get_valid_number("Enter publication year: ")

    book_type = input("Is this an e-book? (y/n): ")
    if book_type.lower() == "y":
        size = get_valid_number("Enter file size in MB: ")
        manager.add_book(EBook(title, author, year, size))
    else:
        manager.add_book(Book(title, author, year))


def main():
    # Main program: menu loop connecting the user to BookManager
    manager = BookManager()
    manager.load_from_file()

    while True:
        print("\n===== Book Management System =====")
        print("1 - Add a new book")
        print("2 - Show all books")
        print("3 - Search book by title")
        print("4 - Save books to file")
        print("5 - Clear all data")
        print("6 - Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_book_menu(manager)
        elif choice == "2":
            manager.show_all_books()
        elif choice == "3":
            search_title = input("Enter title to search: ")
            manager.search_by_title(search_title)
        elif choice == "4":
            manager.save_to_file()
        elif choice == "5":
            manager.clear_file()
        elif choice == "6":
            manager.save_to_file()  # auto-save before exit
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


main()
