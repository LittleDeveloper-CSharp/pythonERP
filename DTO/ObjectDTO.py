class ObjectModel:
    def __init__(self, object_array):
        self.Id = object_array[0]
        self.Name = object_array[1]
        self.rentPrice = object_array[2]
        self.Area = object_array[3]
        self.isActive = object_array[5]
        photoPath = object_array[4]
        if photoPath is None:
            photoPath = '../Resourses/image/none.jpg'
        self.Photo = self.__get_photo(photoPath)

    def __get_photo(self, path):
        import os
        from PIL import Image, ImageTk
        path = os.path.abspath(path)
        sourcePhoto = Image.open(path)
        photo = sourcePhoto.resize((200, 200))
        photoTK = ImageTk.PhotoImage(photo)
        return photoTK
