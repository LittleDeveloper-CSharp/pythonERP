def set_photo(path):
    import os
    from PIL import Image, ImageTk
    if path is None:
        path = '../Resources/image/none.jpg'
    path = os.path.abspath(path)
    source_photo = Image.open(path)
    photo = source_photo.resize((200, 200))
    return ImageTk.PhotoImage(photo)
