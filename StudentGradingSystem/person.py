from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.__name = name #Encapsulation

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name:
            self.__name = new_name
        else:
            print("Invalid name!")

    @abstractmethod
    def display(self):
        pass