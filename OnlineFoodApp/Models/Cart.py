class Cart:
    def __init__(self):
        self.items = {}  # Format: {food_item_object: quantity}
        self.total = 0

    def add_item(self, food_item, quantity=1):
        if food_item in self.items:
            self.items[food_item] += quantity
        else:
            self.items[food_item] = quantity
        self._update_total()
        print(f"Added {quantity}x {food_item.Name} to cart")

    def remove_item(self, food_item, quantity=1):
        """Remove items from cart"""
        if food_item in self.items:
            if self.items[food_item] <= quantity:
                del self.items[food_item]
            else:
                self.items[food_item] -= quantity
            self._update_total()
            print(f"Removed {quantity}x {food_item.Name} from cart")
        else:
            print("Item not found in cart")

    def _update_total(self):
        self.total = sum(item.Price * qty for item, qty in self.items.items())

    def view_cart(self):
        print("\n🛒 Your Cart:")
        if not self.items:
            print("Your cart is empty")
            return False

        for i, (item, qty) in enumerate(self.items.items(), 1):
            print(f"{i}. {item.Name} x{qty} - ₹{item.Price * qty}")
        print(f"\n💵 Total: ₹{self.total}")
        return True

    def checkout(self):
        if not self.view_cart():
            return

        print("\n🔹 Checkout Options:")
        print("1. Proceed to Payment")
        print("2. Continue Shopping")

        try:
            choice = int(input("Select option: "))
            if choice == 1:
                self._process_payment()
                return True  # Order completed
        except ValueError:
            print("Invalid input")
        return False  # Continue shopping

    def _modify_cart(self):
        """Edit cart items/quantities"""
        while True:
            self.view_cart()
            print("\n1. Change quantity")
            print("2. Remove item")
            print("3. Back to checkout")

            try:
                option = int(input("Select action: "))
                if option == 1:
                    self._change_quantity()
                elif option == 2:
                    self._remove_items()
                elif option == 3:
                    break
                else:
                    print("Invalid option")
            except ValueError:
                print("Please enter a number")

    def _change_quantity(self):
        """Modify item quantities"""
        items_list = list(self.items.keys())
        try:
            item_idx = int(input("Enter item number: ")) - 1
            if 0 <= item_idx < len(items_list):
                new_qty = int(input(f"Enter new quantity for {items_list[item_idx].Name}: "))
                if new_qty > 0:
                    self.items[items_list[item_idx]] = new_qty
                    self._update_total()
                else:
                    print("Quantity must be at least 1")
            else:
                print("Invalid item number")
        except ValueError:
            print("Please enter valid numbers")

    def _remove_items(self):
        """Remove items completely"""
        items_list = list(self.items.keys())
        try:
            item_idx = int(input("Enter item number to remove: ")) - 1
            if 0 <= item_idx < len(items_list):
                del self.items[items_list[item_idx]]
                self._update_total()
            else:
                print("Invalid item number")
        except ValueError:
            print("Please enter a valid number")

    def _process_payment(self):
        print("\n💳 Payment Methods:")
        print("1. UPI")
        print("2. Credit/Debit Card")
        print("3. Net Banking")

        try:
            method = int(input("Select payment method: "))
            if method in (1, 2, 3):
                print(f"\n✅ Payment of ₹{self.total} successful!")
                print("Thank you for your order!")
                self.items = {}
                self.total = 0
            else:
                print("Invalid selection")
        except ValueError:
            print("Invalid input")