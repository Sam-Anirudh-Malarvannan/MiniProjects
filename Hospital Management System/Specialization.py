from Patient import Patient

class Specialization:
    MAX_CAPACITY = 20
    PATIENT_STATUS_NUMBERS = [0, 1, 2]

    def __init__(self, name):
        self.name = 'Specialization ' + name
        self.queue = []

    def add_new_patient(self, name, status, print_info=True):
        if len(self.queue) >= self.MAX_CAPACITY:
            if print_info:
                print("APOLOGIES!!! the queue for this specialization is Full.")
            return

        if status not in self.PATIENT_STATUS_NUMBERS:
            if print_info:
                print("Invalid patient status number. It should be 0[Normal], 1[Urgent], 2[Very Urgent]")
            return

        new_patient = Patient(name, status)
        self.queue.append(new_patient)
        self.queue.sort(key=lambda x: x.status, reverse=True)

        if print_info:
            print(f"Patient: {new_patient.name} is {self.format_patient_status(new_patient.status)}")

    def get_next_patient(self):
        if len(self.queue) == 0:
            print("The Queue is Empty")
            return
        next_patient = self.queue.pop(0)
        print(f'{next_patient.name}, Please Go with The Doctor')

    def remove_patient(self, name):
        patients_to_remove = [patient for patient in self.queue if patient.name == name]
        for patient in patients_to_remove:
            self.queue.remove(patient)
            print(f"Patient {patient.name} is Leaving ...")
        return len(patients_to_remove) > 0

    def is_full(self):
        return len(self.queue) >= self.MAX_CAPACITY

    def __str__(self):
        return f"{self.name}: There are {len(self.queue)} Patients"

    @staticmethod
    def format_patient_status(status):
        if status == 0:
            return "Normal"
        elif status == 1:
            return "Urgent"
        else:
            return "Very Urgent"

    def print_patients(self):
        for patient in self.queue:
            print(f"Patient: {patient.name} is {self.format_patient_status(patient.status)}")
