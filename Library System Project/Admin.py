# Import statement - brings Books class from Books module for composition relationship
from Books import Books
# Import statement - brings User class from User module for composition relationship
from User import User


# Class definition - creates Admin class (main controller class in OOP design)
class Admin:
    # Constructor method - special method called when object is created (__init__ is a magic method)
    def __init__(self):
        # Instance variable - dictionary to store user objects (composition - Admin HAS users)
        self.users = {}  # {user_id: User}
        # Instance variable - dictionary to store book objects (composition - Admin HAS books)
        self.books = {}  # {book_id: Book}

    # Method definition - instance method to add books (encapsulation - bundles data and methods)
    def add_book(self, book_id, book_name, book_quantity):
        # Docstring - documentation string explaining method purpose
        """Add a new book to the library"""
        # Conditional statement - checks if book already exists using 'in' operator
        if book_id in self.books:
            # Built-in function - prints message to console
            print("Book already exists")
            # Return statement - exits method early with False value
            return False
        # Dictionary assignment - creates new Books object and stores in books dictionary
        self.books[book_id] = Books(book_name, book_id, book_quantity)
        # Built-in function - prints success message
        print("Book added successfully!")
        # Return statement - exits method with True value indicating success
        return True

    # Method definition - instance method to display all books
    def print_all_books(self):
        # Docstring - explains method functionality
        """Display all books in the library"""
        # Conditional statement - checks if books dictionary is empty (falsy values)
        if not self.books:
            # Return statement - returns string message if no books exist
            return "No books available"
        # Return statement with list comprehension and join method
        return "\n".join([f"ID: {book_id}, Name: {book.name}, Qty: {book.quantity}"
                          # List comprehension - iterates through dictionary items
                          for book_id, book in self.books.items()])

    # Method definition - instance method for searching books
    def search_book(self, query):
        # Docstring - explains search functionality
        """Search for books by name"""
        # Conditional statement - checks if query is empty or None
        if not query:
            # Return statement - returns empty list if no query provided
            return []
        # Return statement with list comprehension for filtering
        return [book for book in self.books.values()
                # Conditional expression - filters books containing query (case-insensitive)
                if query.lower() in book.name.lower()]

    # Method definition - instance method to add users
    def add_user(self, user_id, user_name):
        # Docstring - explains user addition functionality
        """Add a new user to the system"""
        # Conditional statement - checks if user already exists
        if user_id in self.users:
            # Built-in function - prints error message
            print("User already exists")
            # Return statement - exits with False indicating failure
            return False
        # Dictionary assignment - creates new User object and stores it
        self.users[user_id] = User(user_name, user_id)
        # Built-in function - prints success message
        print("User added successfully!")
        # Return statement - exits with True indicating success
        return True

    # Method definition - instance method for book borrowing logic
    def borrow_book(self, user_id, book_id):
        # Docstring - explains borrowing functionality
        """Allow a user to borrow a book"""
        # Conditional statement - validates user exists
        if user_id not in self.users:
            # Return statement - returns error message string
            return "User not found"
        # Conditional statement - validates book exists
        if book_id not in self.books:
            # Return statement - returns error message string
            return "Book not found"
        # Conditional statement - checks book availability
        if self.books[book_id].quantity <= 0:
            # Return statement - returns out of stock message
            return "Book out of stock"

        # Comment explaining business logic check
        # Check if user already borrowed this book
        # Conditional statement - prevents duplicate borrowing
        if book_id in self.users[user_id].borrowed_books:
            # Return statement - returns duplicate borrowing error
            return "User has already borrowed this book"

        # Assignment statement - decrements book quantity (state modification)
        self.books[book_id].quantity -= 1
        # Method call - adds book to user's borrowed books list
        self.users[user_id].borrowed_books.append(book_id)
        # Return statement - returns success message with f-string formatting
        return f"Book '{self.books[book_id].name}' borrowed successfully"

    # Method definition - instance method for book returning logic
    def return_book(self, user_id, book_id):
        # Docstring - explains returning functionality
        """Allow a user to return a borrowed book"""
        # Conditional statement - validates user exists
        if user_id not in self.users:
            # Return statement - returns error message
            return "User not found"
        # Conditional statement - validates book exists
        if book_id not in self.books:
            # Return statement - returns error message
            return "Book not found"
        # Conditional statement - checks if user actually borrowed the book
        if book_id not in self.users[user_id].borrowed_books:
            # Return statement - returns error for book not borrowed
            return "User hasn't borrowed this book"

        # Assignment statement - increments book quantity (state restoration)
        self.books[book_id].quantity += 1
        # Method call - removes book from user's borrowed books list
        self.users[user_id].borrowed_books.remove(book_id)
        # Return statement - returns success message with f-string
        return f"Book '{self.books[book_id].name}' returned successfully"

    # Method definition - instance method to display borrowed books
    def print_borrowed_books(self):
        # Docstring - explains borrowed books display functionality
        """Display all borrowed books by all users"""
        # Variable assignment - creates empty list to store borrowed information
        borrowed_info = []
        # For loop - iterates through all user objects
        for user in self.users.values():
            # Conditional statement - checks if user has borrowed books
            if user.borrowed_books:
                # List comprehension - gets book names from book IDs
                book_names = [self.books[book_id].name for book_id in user.borrowed_books
                              # Conditional expression - ensures book still exists
                              if book_id in self.books]
                # Method call - adds formatted string to borrowed_info list
                borrowed_info.append(f"User: {user.name}, Books: {', '.join(book_names)}")

        # Conditional statement - checks if any books are borrowed
        if not borrowed_info:
            # Return statement - returns message if no books borrowed
            return "No books are currently borrowed"
        # Return statement - joins all borrowed information with newlines
        return "\n".join(borrowed_info)

    # Method definition - instance method to display all users
    def print_all_users(self):
        # Docstring - explains user display functionality
        """Display all users in the system"""
        # Conditional statement - checks if users dictionary is empty
        if not self.users:
            # Return statement - returns message if no users exist
            return "No users registered"
        # Return statement with list comprehension and join method
        return "\n".join([f"ID: {user_id}, Name: {user.name}"
                          # List comprehension - iterates through user dictionary items
                          for user_id, user in self.users.items()])

    # Method definition - instance method to get specific user's borrowed books
    def get_user_borrowed_books(self, user_id):
        # Docstring - explains functionality for getting user's borrowed books
        """Get books borrowed by a specific user"""
        # Conditional statement - validates user exists
        if user_id not in self.users:
            # Return statement - returns error message
            return "User not found"

        # Variable assignment - gets user object reference
        user = self.users[user_id]
        # Conditional statement - checks if user has no borrowed books
        if not user.borrowed_books:
            # Return statement - returns message with f-string formatting
            return f"User {user.name} has no borrowed books"

        # List comprehension - converts book IDs to book names
        book_names = [self.books[book_id].name for book_id in user.borrowed_books
                      # Conditional expression - ensures book exists
                      if book_id in self.books]
        # Return statement - returns formatted string with user's borrowed books
        return f"User {user.name} has borrowed: {', '.join(book_names)}"

    # Method definition - instance method to remove books from system
    def remove_book(self, book_id):
        # Docstring - explains book removal functionality
        """Remove a book from the library (only if not borrowed)"""
        # Conditional statement - validates book exists
        if book_id not in self.books:
            # Return statement - returns error message
            return "Book not found"

        # Comment explaining business logic check
        # Check if book is currently borrowed
        # For loop - iterates through all users
        for user in self.users.values():
            # Conditional statement - checks if book is in user's borrowed books
            if book_id in user.borrowed_books:
                # Return statement - prevents removal if book is borrowed
                return "Cannot remove book - currently borrowed by users"

        # Method call - removes book from dictionary and stores reference
        removed_book = self.books.pop(book_id)
        # Return statement - returns success message with removed book name
        return f"Book '{removed_book.name}' removed successfully"

    # Method definition - instance method to remove users from system
    def remove_user(self, user_id):
        # Docstring - explains user removal functionality
        """Remove a user from the system (only if no borrowed books)"""
        # Conditional statement - validates user exists
        if user_id not in self.users:
            # Return statement - returns error message
            return "User not found"

        # Variable assignment - gets user object reference
        user = self.users[user_id]
        # Conditional statement - checks if user has borrowed books
        if user.borrowed_books:
            # Return statement - prevents removal if user has borrowed books
            return "Cannot remove user - has borrowed books that need to be returned first"

        # Method call - removes user from dictionary and stores reference
        removed_user = self.users.pop(user_id)
        # Return statement - returns success message with removed user name
        return f"User '{removed_user.name}' removed successfully"

    # Method definition - instance method to get detailed book information
    def get_book_details(self, book_id):
        # Docstring - explains book details functionality
        """Get detailed information about a specific book"""
        # Conditional statement - validates book exists
        if book_id not in self.books:
            # Return statement - returns error message
            return "Book not found"

        # Variable assignment - gets book object reference
        book = self.books[book_id]
        # Return statement - returns formatted string with book details
        return f"Book ID: {book_id}, Name: {book.name}, Available Quantity: {book.quantity}"