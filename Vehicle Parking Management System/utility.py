import csv
from owner import VehicleOwner

def load_owner(filename):
    owners = {}

    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)       #Reading a Csv File with Header as Keys
            for row in reader:
                owner = VehicleOwner(row)
                owners[owner.owner_id] = owner

    except FileNotFoundError:
        print('File not found')

    return owners

