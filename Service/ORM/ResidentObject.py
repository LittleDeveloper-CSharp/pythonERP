from DTO.RentObjectDTO import RentObject
from Models.ResidentObject import GetRentObject

def get_resident_object(residentId):
    return list(RentObject(i) for i in GetRentObject(residentId))
