from EmployeesManager import *
from Utility import *

class FrontEndManager:

    def __init__(self):
        self.employees_manager = EmployeesManager()

    def print_menu(self):
        print("\nProgram Options")
        messages = [
            '1) Add a New Employee',
            '2) List all the Employees',
            '3) Delete by Age Range',
            '4) Update Salary by Name',
            '5) End the Program'
        ]
        print('\n'.join(messages))
        msg = f'Enter the choice (from 1 to {len(messages)}): '
        return input_is_valid(msg, 1, len(messages))

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.employees_manager.add_employee()

            elif choice == 2:
                self.employees_manager.list_employee()

            elif choice == 3:
                age_from = input_is_valid("Enter the starting age: ")
                age_to = input_is_valid("Enter the ending age: ")
                self.employees_manager.delete_employees_with_age(age_from, age_to)

            elif choice == 4:
                name = input("Enter the employee's name: ")
                salary = input_is_valid("Enter the new salary: ")
                self.employees_manager.update_salary_by_name(name, salary)

            else:
                print("Exiting Program...")
                break
