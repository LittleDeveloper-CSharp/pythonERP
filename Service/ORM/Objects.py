from DTO.object_market_place import ObjectModel


def get_objects():
    from Models import object_market_place_model
    return [ObjectModel(i) for i in object_market_place_model.get_objects()]
