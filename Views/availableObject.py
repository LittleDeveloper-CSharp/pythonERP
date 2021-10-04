from Models.ObjectModel import ObjectModel
from Models.residentModel import GetFreeObject

def get_available_object():
    return list(ObjectModel(i) for i in GetFreeObject())
