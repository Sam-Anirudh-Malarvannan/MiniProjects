# Class definition - creates Books class (entity class in OOP design pattern)
class Books:
    # Constructor method - special method for object initialization (__init__ is a magic method)
    def __init__(self, name, id, quantity):
        # Instance variable - stores book name (encapsulation - data hiding within object)
        self.name = name
        # Instance variable - stores unique book identifier (attribute of Books class)
        self.id = id
        # Instance variable - stores available quantity (state of the object)
        self.quantity = quantity