class Vehicle:
    def __init__(self, vehicle_no, vehicle_type, owner_id):

        self.__vehicle_no = vehicle_no
        self.__vehicle_type = vehicle_type
        self.__owner_id = owner_id

    @property
    def vehicle_no(self):
        return self.__vehicle_no

    @property
    def vehicle_type(self):
        return self.__vehicle_type

    @property
    def owner_id(self):
        return self.__owner_id