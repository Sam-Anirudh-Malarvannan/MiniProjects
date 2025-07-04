from OnlineFoodApp.Controllers.FoodManager import FoodManager
from OnlineFoodApp.Models.Cart import Cart


class MainMenu:
    __Options = {
        1: "ShowRestaurants",
        2: "ShowFoodItems",
        3: "SearchRestaurant",
        4: "SearchFooditems",
        5: "Logout"
    }

    def __init__(self):
        self.__FoodManager = FoodManager()
        self.__current_cart = Cart()

    def ShowRestaurants(self):
        print("\nAvailable Restaurants:")
        for i, res in enumerate(self.__FoodManager.Restaurants, 1):
            res.DisplayItem(i)

        try:
            choice = int(input("\nSelect a restaurant (number): ")) - 1
            if 0 <= choice < len(self.__FoodManager.Restaurants):
                selected_restaurant = self.__FoodManager.Restaurants[choice]
                self.ShowFoodMenus(selected_restaurant.FoodMenus)
            else:
                print("Invalid selection")
        except ValueError:
            print("Please enter a valid number")

    def ShowFoodItems(self, foodItems):
        print("\nAvailable Food Items:")
        for i, item in enumerate(foodItems, 1):
            item.DisplayItem(i)

        while True:
            try:
                choices = input("\nEnter item numbers to add (comma separated) or 'C' to checkout: ")
                if choices.upper() == 'C':
                    if self.__current_cart.items:
                        self.__current_cart.checkout()
                        break
                    print("Your cart is empty!")
                    continue

                selected = [int(c) - 1 for c in choices.split(',') if c.strip().isdigit()]
                valid_items = [i for i in selected if 0 <= i < len(foodItems)]

                if valid_items:
                    for idx in valid_items:
                        try:
                            qty = int(input(f"How many {foodItems[idx].Name}? (Default 1): ") or 1)
                            self.__current_cart.add_item(foodItems[idx], qty)
                        except ValueError:
                            print("Invalid quantity, defaulting to 1")
                            self.__current_cart.add_item(foodItems[idx])
                else:
                    print("No valid items selected")

                self.__current_cart.view_cart()
            except Exception as e:
                print(f"Error: {e}")

    def SearchRestaurant(self):
        resName = input("Enter Restaurant Name: ")
        res = self.__FoodManager.FindRestaurants(resName)

        if res is not None:
            print("Restaurant Found")
            print(f'>> Restaurant: {res.Name}, Rating: {res.Rating}')
            self.ShowFoodMenus(res.FoodMenus)
        else:
            print("Restaurant Not Found")

    def ShowFoodMenus(self, menus):
        print("\nFood Menus Available:")
        for i, menu in enumerate(menus, 1):
            menu.DisplayItem(i)

        try:
            choice = int(input("\nSelect a menu (number): ")) - 1
            if 0 <= choice < len(menus):
                self.ShowFoodItems(menus[choice].FoodItems)
            else:
                print("Invalid selection")
        except ValueError:
            print("Please enter a valid number")

    def Logout(self):
        print("Logged out successfully. Returning to login screen...")
        return True

    def start(self):
        while True:
            print("\n=== Main Menu ===")
            for option in self.__Options:
                print(f"{option}. {self.__Options[option]}", end=" ")
            print()

            try:
                choice = int(input("Please enter Your Choice: "))
                if choice == 5:  # Logout option
                    print("Logging out...")
                    return

                method = self.__Options.get(choice)
                if method:
                    getattr(self, method)()
                else:
                    print("Invalid choice")
            except ValueError:
                print("Invalid input. Please enter a valid choice.")