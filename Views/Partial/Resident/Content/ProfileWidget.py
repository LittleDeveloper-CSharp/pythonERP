from tkinter import Label, Button, Frame

from Models.ObjectModel import get_details_info


class Profile(Frame):
    def __init__(self, resident_id):
        super().__init__()
        resident_tuple = get_details_info(resident_id)
        photo_path = resident_tuple[8]
        if photo_path is None:
            photo_path = '../Resources/image/emptyPeople.png'
        self.__set_photo(photo_path)
        frame_information = Frame(self)
        Label(frame_information, text=f"Фамилия: {resident_tuple[1]}").pack()
        Label(frame_information, text=f"Имя: {resident_tuple[2]}").pack()
        Label(frame_information, text=f"Отчество: {resident_tuple[3]}").pack()
        Label(frame_information, text=f"ИНН: {resident_tuple[4]}").pack()
        Label(frame_information, text=f"Телефон: {resident_tuple[5]}").pack()
        Label(frame_information, text=f"Email: {resident_tuple[6]}").pack()
        Button(frame_information, text="Редактировать").pack()

        frame_information.grid(row=0, column=1)

    def __set_photo(self, path):
        import os
        from PIL import Image, ImageTk
        path = os.path.abspath(path)
        source_photo = Image.open(path)
        photo = source_photo.resize((200, 200))
        Label(self, image=ImageTk.PhotoImage(photo)).grid(row=0, column=0)
