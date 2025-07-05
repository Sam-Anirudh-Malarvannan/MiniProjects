from Utility import *
from Employee import *

class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        print("\nEnter Employee Data")
        name = input("Enter Employee Name: ")
        age = input_is_valid("Enter Employee Age: ")
        salary = input_is_valid("Enter Employee Salary: ")
        self.employees.append(Employee(name, age, salary))

    def list_employee(self):
        if len(self.employees) == 0:
            print("Employee List is Empty!")
            return
        for emp in self.employees:
            print(emp)

    def delete_employees_with_age(self, age_from, age_to):
        to_delete = [emp for emp in self.employees if age_from <= int(emp.age) <= age_to]
        for emp in to_delete:
            print(f"Deleting Employee {emp.name}")
            self.employees.remove(emp)

    def find_employee_by_name(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def update_salary_by_name(self, name, salary):
        emp = self.find_employee_by_name(name)
        if emp is None:
            print("Error: No Employee Found")
        else:
            emp.salary = salary
            print(f"Updated {emp.name}'s salary to {emp.salary}")
