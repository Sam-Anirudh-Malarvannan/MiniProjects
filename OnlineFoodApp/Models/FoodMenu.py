from OnlineFoodApp.Models.AbstractItem import AbstractItem
from OnlineFoodApp.Models.FoodItems import FoodItems

class FoodMenu(AbstractItem):
    def __init__(self, name, rating=0.0):
        super().__init__(name, rating)
        self.__FoodItems = []

    @property
    def FoodItems(self):
        return self.__FoodItems

    @FoodItems.setter
    def FoodItems(self, items):
        for item in items:
            if not isinstance(item, FoodItems):
                raise ValueError("Invalid FoodItem")
        self.__FoodItems = items

    def DisplayItem(self, idx):
        print(f"{idx}. {self.Name} (Rating: {self.Rating})")