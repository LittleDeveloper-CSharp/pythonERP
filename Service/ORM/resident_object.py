from DTO.rent_object import RentObject
from Models.resident_object import get_rent_object


def get_resident_object(resident_id):
    return list(RentObject(i) for i in get_rent_object(resident_id))
