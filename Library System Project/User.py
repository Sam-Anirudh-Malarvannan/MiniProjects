# Class definition - creates User class (entity class representing library users)
class User:
    # Constructor method - special method called when User object is created
    def __init__(self, name, id):
        # Instance variable - stores user's name (encapsulation - data is bound to object)
        self.name = name
        # Instance variable - stores unique user identifier (attribute of User class)
        self.id = id
        # Instance variable - list to track borrowed books (composition - User HAS borrowed books)
        self.borrowed_books = []  # Track borrowed books