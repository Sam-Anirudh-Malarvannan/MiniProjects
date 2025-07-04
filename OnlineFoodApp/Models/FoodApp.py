from User import User
from UserManager import UserManager
from OnlineFoodApp.Controllers.MainMenu import MainMenu
import re

class LoginSystem:
    def Login(self):
        mailid = input("Email: ")
        password = input("Password: ")

        user = UserManager.FindUser(mailid, password)

        if user is not None:
            print(f"Welcome back, {user.Name}!")
            MainMenu().start()
        else:
            print("Invalid mailId/Password... Please Retry")

    def Register(self):
        Name = input("Name: ")
        Mobile = input("Mobile Number: ")
        mailid = input("Email: ")
        password = input("Password: ")

        # Validation Section
        if len(Mobile) != 10 or not Mobile.isdigit():
            print("Invalid Mobile Number")
            return

        if len(Name) < 2 or not re.match(r'^[a-zA-Z\s]+$', Name):
            print("Invalid Name")
            return

        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", mailid):
            print("Invalid email")
            return

        if len(password) < 8:
            print("Password must be at least 8 characters long")
            return
        if not re.search(r"[A-Z]", password):
            print("Password must contain at least one uppercase letter")
            return
        if not re.search(r"[a-z]", password):
            print("Password must contain at least one lowercase letter")
            return
        if not re.search(r"\d", password):
            print("Password must contain at least one digit")
            return

        # If all validation passed
        user = User(Name, Mobile, mailid, password)
        if UserManager.AddUser(user):
            print("Registration successful!")

    def GuestLogin(self):
        print("Guest login successful! Enjoy browsing as a guest.")
        MainMenu().start()

    def Exit(self):
        print("Thank you for using our Food App...")
        exit()

    def ValidateOption(self, option):
        getattr(self, option)()

class FoodApp:
    LoginOptions = {
        1: "Login",
        2: "Register",
        3: "GuestLogin",
        4: "Exit"
    }

    @staticmethod
    def Init():
        print("<< Welcome to Online Food Ordering >>")
        loginSystem = LoginSystem()
        while True:
            for option in FoodApp.LoginOptions:
                print(f"{option}. {FoodApp.LoginOptions[option]}", end=" ")
            print()
            try:
                choice = int(input("Please enter Your Choice: "))
                loginSystem.ValidateOption(FoodApp.LoginOptions[choice])
            except (ValueError, KeyError):
                print("Invalid input.. Please enter a valid choice")