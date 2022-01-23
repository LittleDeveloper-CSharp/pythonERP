from DTO.rentObjectDTO import RentObject
from Models.ResidentObject import get_rent_object


def get_resident_object(residentId):
    return list(RentObject(i) for i in get_rent_object(residentId))
