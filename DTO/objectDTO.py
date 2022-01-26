class ObjectModel:
    def __init__(self, object_array):
        self.Id = object_array[0]
        self.Name = object_array[1]
        self.rentPrice = object_array[2]
        self.Area = object_array[3]
        self.idStatus = object_array[5]
        photo_path = object_array[4]
        if photo_path is None:
            photo_path = '../Resources/image/none.jpg'
        self.__set_photo(photo_path)

    def __set_photo(self, path):
        import os
        from PIL import Image, ImageTk
        path = os.path.abspath(path)
        source_photo = Image.open(path)
        photo = source_photo.resize((200, 200))
        self.Photo = ImageTk.PhotoImage(photo)
