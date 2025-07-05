from OperationsManager import OperationsManager
from Utility import generating_random_data

if __name__ == '__main__':
    main = OperationsManager()
    generating_random_data(main)
    main.run()
