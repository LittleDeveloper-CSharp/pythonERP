class RentObject:
    def __init__(self, object_array):
        self.Id = object_array[0]
        self.Name = object_array[1]
        self.Area = object_array[2]
        self.DateStart = object_array[3]
        self.DateEnd = object_array[4]
        self.SumRent = object_array[5]
        self.Photo = self.__get_photo(object_array[6])

    def __get_photo(self, path):
        import os
        from PIL import Image, ImageTk
        path = os.path.abspath(path)
        sourcePhoto = Image.open(path)
        photo = sourcePhoto.resize((200, 200))
        photoTK = ImageTk.PhotoImage(photo)
        return photoTK
