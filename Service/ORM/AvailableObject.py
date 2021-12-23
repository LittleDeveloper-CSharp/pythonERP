from DTO.ObjectDTO import ObjectModel
from Models.ObjectModel import get_free_object

def get_available_object():
    return list(ObjectModel(i) for i in get_free_object())
