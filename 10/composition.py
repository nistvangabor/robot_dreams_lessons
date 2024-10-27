class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def __str__(self):
        return f"{self.name} ({self.nationality})"


class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author  # Author instance, not a string
        self.genre = genre

    def __str__(self):
        return f"'{self.title}' by {self.author} - Genre: {self.genre}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # List to store Book instances

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")

    def list_books(self):
        print(f"\nBooks available in {self.name}:")
        for book in self.books:
            print(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book removed: '{title}'")
                return
        print(f"No book found with the title '{title}'")


# Creating instances of Author
author1 = Author("George Orwell", "British")
author2 = Author("Harper Lee", "American")
print(author1)

# Creating instances of Book with Author composition
book1 = Book("1984", author1, "Dystopian")
book2 = Book("To Kill a Mockingbird", author2, "Classic Fiction")

# Creating an instance of Library and adding books to it
my_library = Library("City Library")
my_library.add_book(book1)
my_library.add_book(book2)

# Listing all books in the library
my_library.list_books()

# Removing a book by title
my_library.remove_book("1984")
my_library.list_books()