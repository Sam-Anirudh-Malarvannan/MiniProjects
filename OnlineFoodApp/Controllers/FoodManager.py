from OnlineFoodApp.Models.FoodItems import FoodItems
from OnlineFoodApp.Models.FoodMenu import FoodMenu
from OnlineFoodApp.Models.Restaurant import Restaurant

class FoodManager:
    def __init__(self):
        self.Restaurants = self.__PrepareRestaurant()

    def __PrepareFoodItems(self):
        items = [
            FoodItems("Veg Biriyani", 4, 150, "Vegetarian biriyani with mixed vegetables"),
            FoodItems("Chicken Biriyani", 4.2, 200, "Authentic chicken biriyani"),
            FoodItems("Parota", 4.4, 50, "Kerala style layered parota"),
            FoodItems("Dosa", 4.1, 80, "South Indian crispy dosa"),
            FoodItems("Noodles", 3.8, 100, "Chinese style hakka noodles")
        ]
        return items

    def __PrepareFoodMenus(self):
        items = self.__PrepareFoodItems()
        menus = [
            FoodMenu("Veg", 4.0),
            FoodMenu("Non-Veg", 4.2),
            FoodMenu("Chinese", 3.9)
        ]
        menus[0].FoodItems = [items[0], items[3]]
        menus[1].FoodItems = [items[1], items[2]]
        menus[2].FoodItems = [items[4]]
        return menus

    def __PrepareRestaurant(self):
        menus = self.__PrepareFoodMenus()
        restaurants = [
            Restaurant("A2B", 4, "Chennai", 10),
            Restaurant("Mani", 4.8, "Mettupalayam", 18),
            Restaurant("HMR", 4.2, "Coimbatore", 14)
        ]
        restaurants[0].FoodMenus = [menus[0]]
        restaurants[1].FoodMenus = [menus[0], menus[1]]
        restaurants[2].FoodMenus = [menus[1], menus[2]]
        return restaurants

    def FindRestaurants(self, name):
        for res in self.Restaurants:
            if res.Name.lower() == name.lower():
                return res
        return None