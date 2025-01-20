class Book:
  """Represents a book with title, author, and availability."""

  def __init__(self, title, author):
    """Initializes a Book instance."""
    self.title = title
    self.author = author
    self._is_checked_out = False  # Private attribute to track availability

  def is_checked_out(self):
    """Returns True if the book is checked out, False otherwise."""
    return self._is_checked_out
  
  def return_book(self, title):
    """Returns a book by title.

    Args:
      title: The title of the book to return.

    Returns:
      A message indicating success or failure.
    """
    for book in self._books:
      if book.title == title and book.is_checked_out():
        book._is_checked_out = False
        return f"Successfully returned '{title}'."
    return f"Sorry, '{title}' is not currently checked out."

class Library:
  """Represents a library with a collection of books."""

  def __init__(self):
    """Initializes a Library instance."""
    self._books = []  # Private list to store Book instances

  def add_book(self, book):
    """Adds a book to the library's collection."""
    self._books.append(book)

  def check_out_book(self, title):
    """Checks out a book by title if available.

    Args:
      title: The title of the book to check out.

    Returns:
      A message indicating success or failure.
    """
    for book in self._books:
      if book.title == title and not book.is_checked_out():
        book._is_checked_out = True
        return f"Successfully checked out '{title}'."
    return f"Sorry, '{title}' is not available for checkout."

  def return_book(self, title):
    """Returns a book by title.

    Args:
      title: The title of the book to return.

    Returns:
      A message indicating success or failure.
    """
    for book in self._books:
      if book.title == title and book.is_checked_out():
        book._is_checked_out = False
        return f"Successfully returned '{title}'."
    return f"Sorry, '{title}' is not currently checked out."

  def list_available_books(self):
    """Lists all available books in the library."""
    available_books = []
    for book in self._books:
      if not book.is_checked_out():
        available_books.append(book.title)
    if not available_books:
      return "There are currently no available books in the library."
    return f"Available books: {', '.join(available_books)}"