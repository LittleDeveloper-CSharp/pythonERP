class ObjectModel:
    def __init__(self, object_array):
        self.Id = object_array[0]
        self.Name = object_array[1]
        self.rentPrice = object_array[2]
        self.Area = object_array[3]
        self.idStatus = object_array[5]
        self.photo_path = object_array[4]
