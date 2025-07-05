from Specialization import Specialization
from Utility import input_is_valid

class OperationsManager:
    def __init__(self):
        self.specs = []

    def print_menu(self):
        print("Program Options: ")
        messages = [
            '1) Add new patients',
            '2) Print all the Patients',
            '3) Get next patient',
            '4) Remove a leaving patient',
            '5) End the program'
        ]
        print('\n'.join(messages))
        msg = f'Enter your choice from 1 to {len(messages)}\n'
        return input_is_valid(msg, 1, len(messages))

    def run(self):
        choice = self.print_menu()
        while True:
            if choice == 1:
                spec_name = input("Enter Specialization: ")
                patient_name = input("Enter the patient's name: ")
                patient_status = int(input("Enter Status (0 Normal / 1 Urgent / 2 Very Urgent): "))

                spec_exist = False
                spec_found = None

                for spec_obj in self.specs:
                    if spec_obj.name == 'Specialization ' + spec_name:
                        spec_exist = True
                        spec_found = spec_obj
                        break

                if spec_exist:
                    spec_found.add_new_patient(patient_name, patient_status)
                else:
                    new_spec = Specialization(spec_name)
                    new_spec.add_new_patient(patient_name, patient_status)
                    self.specs.append(new_spec)

            elif choice == 2:
                for spec in self.specs:
                    print(spec)
                    spec.print_patients()

            elif choice == 3:
                spec_name = input("Enter the Specialization: ")
                found = False
                for spec in self.specs:
                    if spec.name == 'Specialization ' + spec_name:
                        spec.get_next_patient()
                        found = True
                        break
                if not found:
                    print("There is no Specialization with this name.")

            elif choice == 4:
                spec_name = input("Enter the Specialization: ")
                patient_name = input("Enter the patient's name: ")
                for spec in self.specs:
                    if spec.name == 'Specialization ' + spec_name:
                        removed = spec.remove_patient(patient_name)
                        if not removed:
                            print("No patient with such name in this specialization.")
                        spec.print_patients()

            elif choice == 5:
                break
            else:
                print("Invalid Choice, Please Select a Valid Option.")
            choice = self.print_menu()
