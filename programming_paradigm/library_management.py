class Book:
    """Represents a book with a title, author, and availability status."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Private attribute to track availability
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books."""
    def __init__(self):
        # Private list to store Book instances
        self._books = []

    def add_book(self, book):
        """Adds a new Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Finds a book by title and checks it out if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book '{title}' is not available or does not exist.")

    def return_book(self, title):
        """Finds a book by title and returns it to the library."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return

    def list_available_books(self):
        """Prints all books that are currently available."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")