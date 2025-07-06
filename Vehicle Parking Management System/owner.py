class VehicleOwner:
    def __init__(self, data_dict):
        self.data = data_dict  # Store all columns as a dictionary

    @property
    def owner_id(self):
        return self.data.get('owner_id')

    @property
    def name(self):
        return self.data.get('name')

    @property
    def contact(self):
        return self.data.get('contact')

    # Optional: Dynamic access to other fields
    def get_field(self, field_name):
        return self.data.get(field_name)
