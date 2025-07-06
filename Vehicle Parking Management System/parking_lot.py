from parking_slot import ParkingSlot
from Vehicle import Vehicle

class ParkingLot:

    def __init__(self, total_slots):
        self.slots = [ParkingSlot(i + 1) for i in range(total_slots)]

    def park_vehicle(self, vehicle):
        for slot in self.slots:
            if slot.is_available():
                slot.park_vehicle(vehicle)
                return slot.slot_no
        return -1

    def remove_vehicle(self, vehicle_no):
        for slot in self.slots:
            if slot.vehicle and slot.vehicle.vehicle_no == vehicle_no:
                slot.remove_vehicle()
                return True
        return False

    def display_status(self):
        print("\nParking Lot Status")
        for slot in self.slots:
            if slot.is_available():
                print(f'Slot {slot.slot_no} is available')
            else:
                v = slot.vehicle
                print(f'Slot {slot.slot_no}: {v.vehicle_type} [{v.vehicle_no}] Owner Id : {v.owner_id}')
