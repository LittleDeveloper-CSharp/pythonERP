from tkinter import Label, Button, Frame, Toplevel

from DTO.resident import Resident
from Models.ObjectModel import get_details_info
from Views.Partial.Resident.Content.EditProfileResidentFrame import EditProfileResidentFrame


class Profile(Frame):
    def __init__(self, resident_id):
        super().__init__()
        resident = Resident(get_details_info(resident_id))
        photo_path = resident.photo_path
        if photo_path is None:
            photo_path = '../Resources/image/emptyPeople.png'
        self.__set_photo(photo_path)
        frame_information = Frame(self)
        Label(frame_information, text=f"Логин: {resident.login}").pack()
        Label(frame_information, text=f"Фамилия: {resident.last_name}").pack()
        Label(frame_information, text=f"Имя: {resident.first_name}").pack()
        Label(frame_information, text=f"Отчество: {resident.patronymic}").pack()
        Label(frame_information, text=f"ИНН: {resident.inn}").pack()
        Label(frame_information, text=f"Телефон: {resident.phone}").pack()
        Label(frame_information, text=f"Email: {resident.email}").pack()
        Button(frame_information, text="Редактировать", command=lambda: self.__edit_profile_click(resident)).pack()

        frame_information.grid(row=0, column=1)

    def __set_photo(self, path):
        import os
        from PIL import Image, ImageTk
        path = os.path.abspath(path)
        source_photo = Image.open(path)
        photo = source_photo.resize((200, 200))
        image = ImageTk.PhotoImage(photo)
        panel = Label(self)
        panel.grid(row=0, column=0)
        panel.configure(image=image)
        panel.image = image

    def __edit_profile_click(self, resident):
        edit_modal = Toplevel(self)
        EditProfileResidentFrame(edit_modal, resident).pack()
        edit_modal.title("Редактирование")
