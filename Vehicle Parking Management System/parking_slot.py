class ParkingSlot:

    def __init__(self, slot_no):
        self.slot_no = slot_no
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None

    def park_vehicle(self, vehicle):
        if self.is_available():
            self.vehicle = vehicle
            return True
        return False

    def remove_vehicle(self):
        self.vehicle = None