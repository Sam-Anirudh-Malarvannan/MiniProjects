# Comment explaining file purpose - entry point of the application
# main.py
# Import statement - brings all functions/classes from OperationsManager module (wildcard import)
from OperationsManager import *
# Conditional statement - checks if script is run directly (not imported as module)
if __name__ == '__main__':
    # Variable assignment - creates instance of OperationsManager class (object instantiation)
    manager = OperationsManager()
    # Method call - calls run method to start the application (program execution begins)
    manager.run()