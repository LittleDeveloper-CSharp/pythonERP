from DTO.object_market_place import ObjectModel
from Models.object_market_place_model import get_free_object


def get_available_object():
    return list(ObjectModel(i) for i in get_free_object())
