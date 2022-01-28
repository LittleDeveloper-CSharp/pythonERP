from Service.Helper.OpenerPhoto import set_photo


class RequestRentObject:
    def __init__(self, item):
        self.Id = item[0]
        self.RentPrice = item[1]
        self.Area = item[2]
        self.DateStart = item[3]
        self.DateEnd = item[4]
        self.SumRent = item[5]
        self.photo = set_photo(item[6])
