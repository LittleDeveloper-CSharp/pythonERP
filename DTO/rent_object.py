class RentObject:
    def __init__(self, object_array):
        self.Id = object_array[0]
        self.Name = object_array[1]
        self.Area = object_array[2]
        self.DateStart = object_array[3]
        self.DateEnd = object_array[4]
        self.SumRent = object_array[5]
        self.photo_path = object_array[6]
        self.idStatus = object_array[7]
