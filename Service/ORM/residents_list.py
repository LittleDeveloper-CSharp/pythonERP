from DTO.resident import Resident
from Models.admin_model import get_residents


def get_residents_list():
    return [Resident().set_value(i) for i in get_residents()]
