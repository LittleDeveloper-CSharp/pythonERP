def set_photo(path):
    import os
    from PIL import Image, ImageTk
    if path is None:
        path = '../Resources/image/none.jpg'
    path_module = os.path.abspath(__file__).split('\\')
    path_module = '\\'.join(path_module[0:(len(path_module) - 1)])

    full_path = os.path.join(path_module, path)

    path = os.path.abspath(full_path)
    source_photo = Image.open(path)
    photo = source_photo.resize((200, 200))
    return ImageTk.PhotoImage(photo)
