from Student import Student, ScienceStudent

students = {}

def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter the Name : ")

    print("\n1) Regular Student")
    print("2) Science Student")
    choice = input("Enter to Sect Type: ")

    if choice == "2":
        s = ScienceStudent(roll , name)
    else:
        s = Student(roll, name)

    num_subjects = int(input("Number of subjects: "))
    for _ in range(num_subjects):
        subject = input("Subject Name: ")
        mark = float(input(f"Mark in {subject}: "))
        s.add_mark(subject, mark)

    students[roll] = s
    print("Students Added Successfully!\n")

def show_student():
    roll = int(input("Enter the Roll Number: "))
    if roll in students:
        students[roll].display()
    else:
        print("Student Not Found")

def show_all_students():
    if not students:
        print("No students Added yet.")
    for s in students.values():
        s.display()

while True:
    print("\n--- Student Grading ---")
    print("1) Add Student")
    print("2) Show Student by Roll Number")
    print("3) Show All Students ")
    print("4) Exit ")

    option = input("Select option: ")

    if option == "1":
        add_student()

    elif option == "2":
        show_student()

    elif option == "3":
        show_all_students()

    elif option == "4":
        print("Exiting Program")
        break

    else:
        print("Invalid Option")