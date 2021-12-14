from DTO.ObjectDTO import ObjectModel
from Models.ObjectModel import GetFreeObject

def get_available_object():
    return list(ObjectModel(i) for i in GetFreeObject())
