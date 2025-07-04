from OnlineFoodApp.Models.AbstractItem import AbstractItem

class FoodItems(AbstractItem):
    def __init__(self, name, rating, price, description):
        super().__init__(name, rating)
        if price <= 0:
            raise ValueError("Price must be positive")
        if not description.strip():
            raise ValueError("Description cannot be empty")
        self.Price = price
        self.Description = description

    def DisplayItem(self, start):
        print(f"{start} => Name : {self.Name} Price: {self.Price} Rating: {self.Rating} Description: {self.Description}")