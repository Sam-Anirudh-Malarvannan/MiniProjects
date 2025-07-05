from person import Person
from Grading import GradingSystem
class Student(Person, GradingSystem): #Multiple Inheritance
    def __init__(self, roll_no, name):
        super().__init__(name)
        self.__roll_no = roll_no
        self.marks = {}

    @property
    def roll_no(self):
        return self.__roll_no

    def add_mark(self, subject, marks):
        self.marks[subject] = marks

    def total_marks(self):
        return sum(self.marks.values())

    def percentage(self):
        return self.total_marks() /  len(self.marks) if self.marks else 0

    def grade(self):
        pct = self.percentage()
        return self.get_grade(pct)  # Using GradingSystem logic

    def display(self):
        print(f"\n--- Student Details ---")
        print(f"RollNo: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"percentage: {self.percentage():.2f}%")
        print(f"Grade: {self.grade()}")


class ScienceStudent(Student):
    def __init__(self, roll_no, name):
        super().__init__(roll_no, name)
        self.stream = "Science"

    def display(self):
        super().display()
        print(f'Stream: {self.stream}')
