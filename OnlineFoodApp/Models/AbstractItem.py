from abc import ABC, abstractmethod


class AbstractItem(ABC):

    def __init__(self,name, rating):
        self.Name = name
        self.Rating = rating

    @abstractmethod
    def DisplayItem(self, start):
        pass
