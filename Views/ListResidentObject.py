from Models.rentObjectModel import RentObject
from Models.residentModel import GetRentObject

def get_resident_object(residentId):
    return list(RentObject(i) for i in GetRentObject(residentId))
