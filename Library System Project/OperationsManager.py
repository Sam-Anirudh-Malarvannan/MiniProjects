# Import statement - brings Admin class from Admin module (dependency injection)
from Admin import Admin
# Import statement - brings validation function from Utility module (code reuse)
from Utility import input_is_valid


# Class definition - creates OperationsManager class (controller class in MVC pattern)
class OperationsManager:
    # Constructor method - special method for object initialization
    def __init__(self):
        # Instance variable - creates Admin object (composition - OperationsManager HAS Admin)
        self.admin = Admin()

    # Method definition - instance method to display menu options
    def print_menu(self):
        # Variable assignment - creates list of menu options (data structure)
        options = [
            # String literals - menu option descriptions
            '1) Add Book',
            '2) Print Books',
            '3) Search Books',
            '4) Add User',
            '5) Borrow Book',
            '6) Return Book',
            '7) Print Borrowed Books',
            '8) Print Users',
            '9) Exit'
        ]
        # Built-in function - prints formatted header with string multiplication
        print("\n" + "="*40)
        # Built-in function - prints system title
        print("LIBRARY MANAGEMENT SYSTEM")
        # Built-in function - prints separator line
        print("="*40)
        # Built-in function - prints menu options joined with newlines
        print("\n".join(options))
        # Built-in function - prints bottom separator
        print("="*40)
        # Return statement - calls utility function for input validation
        return input_is_valid("Enter choice (1-9): ", 1, 9)

    # Method definition - main method that controls program flow
    def run(self):
        # Infinite loop - keeps program running until user chooses to exit
        while True:
            # Variable assignment - gets user's menu choice
            choice = self.print_menu()

            # Conditional statement - checks if user chose option 1 (Add Book)
            if choice == 1:
                # Built-in function - prints section header
                print("\n--- ADD BOOK ---")
                # Variable assignment - gets book ID from user input
                book_id = input("Enter book ID: ")
                # Variable assignment - gets book name from user input
                name = input("Enter book name: ")
                # Try-except block - handles potential conversion errors
                try:
                    # Variable assignment - converts quantity input to integer
                    qty = int(input("Enter quantity: "))
                    # Method call - calls admin method to add book
                    self.admin.add_book(book_id, name, qty)
                # Exception handling - catches ValueError for invalid integer input
                except ValueError:
                    # Built-in function - prints error message for invalid quantity
                    print("Please enter a valid number for quantity!")

            # Conditional statement - checks if user chose option 2 (Print Books)
            elif choice == 2:
                # Built-in function - prints section header
                print("\n--- ALL BOOKS ---")
                # Built-in function - prints result of admin method call
                print(self.admin.print_all_books())

            # Conditional statement - checks if user chose option 3 (Search Books)
            elif choice == 3:
                # Built-in function - prints section header
                print("\n--- SEARCH BOOKS ---")
                # Variable assignment - gets search query from user
                query = input("Enter search term: ")
                # Variable assignment - gets search results from admin method
                books = self.admin.search_book(query)
                # Conditional statement - checks if books were found
                if books:
                    # Built-in function - prints found books header
                    print("Found books:")
                    # For loop - iterates through found books
                    for book in books:
                        # Built-in function - prints book details with f-string formatting
                        print(f"ID: {book.id}, Name: {book.name}, Qty: {book.quantity}")
                # Else clause - executes when no books found
                else:
                    # Built-in function - prints no results message
                    print("No books found matching your search.")

            # Conditional statement - checks if user chose option 4 (Add User)
            elif choice == 4:
                # Built-in function - prints section header
                print("\n--- ADD USER ---")
                # Variable assignment - gets user ID from input
                user_id = input("Enter user ID: ")
                # Variable assignment - gets user name from input
                name = input("Enter user name: ")
                # Method call - calls admin method to add user
                self.admin.add_user(user_id, name)

            # Conditional statement - checks if user chose option 5 (Borrow Book)
            elif choice == 5:
                # Built-in function - prints section header
                print("\n--- BORROW BOOK ---")
                # Variable assignment - gets user ID from input
                user_id = input("Enter user ID: ")
                # Variable assignment - gets book ID from input
                book_id = input("Enter book ID: ")
                # Variable assignment - gets result from admin borrow method
                result = self.admin.borrow_book(user_id, book_id)
                # Built-in function - prints the result message
                print(result)

            # Conditional statement - checks if user chose option 6 (Return Book)
            elif choice == 6:
                # Built-in function - prints section header
                print("\n--- RETURN BOOK ---")
                # Variable assignment - gets user ID from input
                user_id = input("Enter user ID: ")
                # Variable assignment - gets book ID from input
                book_id = input("Enter book ID: ")
                # Variable assignment - gets result from admin return method
                result = self.admin.return_book(user_id, book_id)
                # Built-in function - prints the result message
                print(result)

            # Conditional statement - checks if user chose option 7 (Print Borrowed Books)
            elif choice == 7:
                # Built-in function - prints section header
                print("\n--- BORROWED BOOKS ---")
                # Built-in function - prints result of admin method call
                print(self.admin.print_borrowed_books())

            # Conditional statement - checks if user chose option 8 (Print Users)
            elif choice == 8:
                # Built-in function - prints section header
                print("\n--- ALL USERS ---")
                # Built-in function - prints result of admin method call
                print(self.admin.print_all_users())

            # Conditional statement - checks if user chose option 9 (Exit)
            elif choice == 9:
                # Built-in function - prints goodbye message
                print("\nThank you for using the Library Management System!")
                # Built-in function - prints exit message
                print("Exiting...")
                # Break statement - exits the while loop and terminates program
                break

            # Comment explaining user experience enhancement
            # Pause for user to see the output
            # Built-in function - waits for user to press Enter before continuing
            input("\nPress Enter to continue...")