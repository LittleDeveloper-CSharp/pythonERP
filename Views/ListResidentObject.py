from Models.ObjectModel import ObjectModel

def get_resident_object():
    objects = (ObjectModel((1, "Кто-то 1", 10, False, r'..\Controllers\image\1.jpg')),
               ObjectModel((2, "Кто-то 2", 321, False, r'..\Controllers\image\2.jpg')),
               ObjectModel((4, "Кто-то 4", 453, False, r'..\Controllers\image\4.jpg')),
               ObjectModel((7, "Кто-то 7", 654, False, r'..\Controllers\image\7.jpg')))

    return objects

