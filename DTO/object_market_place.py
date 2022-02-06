class ObjectModel:
    Id = None,
    Name = None,
    rentPrice = None,
    Area = None,
    photo_path = None,
    idStatus = None

    def set_value(self, object_array):
        self.Id = object_array[0]
        self.Name = object_array[1]
        self.rentPrice = object_array[2]
        self.Area = object_array[3]
        self.photo_path = object_array[4]
        self.idStatus = object_array[5]

        return self
