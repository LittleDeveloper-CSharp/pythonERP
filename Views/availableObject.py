from Models.ObjectModel import ObjectModel

def get_available_object():
    objects = (ObjectModel((1, "Кто-то 1", 10, True, r'..\Controllers\image\1.jpg')),
               ObjectModel((2, "Кто-то 2", 321, True, r'..\Controllers\image\2.jpg')),
               ObjectModel((3, "Кто-то 3", 423, True, r'..\Controllers\image\3.jpg')),
               ObjectModel((4, "Кто-то 4", 453, True, r'..\Controllers\image\4.jpg')),
               ObjectModel((5, "Кто-то 5", 345, True, r'..\Controllers\image\5.jpg')),
               ObjectModel((6, "Кто-то 6", 234, True, r'..\Controllers\image\6.jpg')),
               ObjectModel((7, "Кто-то 7", 654, True, r'..\Controllers\image\7.jpg')))
    return objects
