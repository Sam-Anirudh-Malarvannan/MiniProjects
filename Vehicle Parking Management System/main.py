from Vehicle import Vehicle
from parking_lot import ParkingLot
from utility import load_owner

owners = load_owner('owner.csv')
parking_lot = ParkingLot(total_slots = 5)

while True:
    print("\nVehicle Parking Management System")
    print("1) Park Vehicles")
    print("2) Remove Vehicles")
    print("3) Show Vehicle Status")
    print("4) List Owners")
    print("5) Exit")

    choice = input("Choose a Option").strip()

    if choice == "1":
        vehicle_no = input("Enter Vehicle Number : ")
        vehicle_type = input("Enter the Vehicle Type : ")
        owner_id = input("Enter Owner Id : ")

        if owner_id in owners:
            vehicle = Vehicle(vehicle_no, vehicle_type, owner_id)
            slot = parking_lot.park_vehicle(vehicle)
            if slot != -1:
                print(f'Vehicle Parked in {slot}')
            else:
                print("Parking Slot is Full!!!")

    elif choice == "2":
        vehicle_no = input("Enter Vehicle Number : ")
        if parking_lot.remove_vehicle(vehicle_no):
            print("The Vehicle from the Parking Lot has been removed")
        else:
            print("Vehicle Not Found!")

    elif choice == "3":
        parking_lot.display_status()

    elif choice == "4":
        print("\nRegistered Owners:")
        for owner in owners.values():
            print(f"ID: {owner.owner_id} | Name: {owner.name} | Contact: {owner.contact}")

    elif choice == "5":
        print("Exiting the Program")
        break

    else:
        print("Invalid Choice")