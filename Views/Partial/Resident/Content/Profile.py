from tkinter import Label, Button, Frame

from Models.ObjectModel import GetDetailsInfo


class Profile(Frame):
    def __init__(self, root, resident_id):
        Frame().__init(self, root)
        resident_tuple = GetDetailsInfo(resident_id)
        Label(root, image="").pack()
        Label(root, text=f"Фамилия: {resident_tuple[1]}").pack()
        Label(root, text=f"Имя: {resident_tuple[2]}").pack()
        Label(root, text=f"Отчество: {resident_tuple[3]}").pack()
        Label(root, text=f"ИНН: {resident_tuple[4]}").pack()
        Label(root, text=f"Телефон: {resident_tuple[5]}").pack()
        Label(root, text=f"Email: {resident_tuple[6]}").pack()
        Button(root, text="Редактировать").pack()