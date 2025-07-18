from Specialization import Specialization
import random

def input_is_valid(msg, start=0, end=None):
    while True:
        inp = input(msg)
        if not inp.isdecimal():
            print("Invalid Input, Try Again")
        elif start is not None and end is not None:
            if not(start <= int(inp) <= end):
                print("Invalid Input, Try Again")
            else:
                return int(inp)
        else:
            return int(inp)

def generating_random_data(main_app):
    import random
    for i in range(1, 6):
        new_spec = Specialization(str(i))
        for j in range(6):
            dummy = f'dummy{j}'
            new_spec.add_new_patient(dummy, random.randint(0, 2), print_info=False)
        main_app.specs.append(new_spec)
