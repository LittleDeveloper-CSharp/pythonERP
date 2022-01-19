from Models.ResidentObject import get_rent_object, cancellation_rent
from tkinter import Frame, Label, Button, Toplevel, messagebox
import math

from DTO.rentObjectDTO import RentObject
from Views.ObjectDetailsInfo import DetailsInfo


class RentObjectWidget(Frame):
    def __init__(self, master, resident_id):
        super().__init__(master)
        resident_objects = get_rent_object(resident_id)

        self.resident_id = resident_id

        objects = [RentObject(i) for i in resident_objects]

        count_row = math.ceil(len(objects) / 10)
        count_object = len(objects)
        index = 0

        if count_object == 0:
            Label(self, text="Информация отсутствует").pack()
            return

        for i in range(count_row):
            for j in range(10):
                obj_frame = Frame(self)
                rent_object = objects[index]
                image_object = Label(obj_frame)

                image_object.pack()
                image_object.configure(image=rent_object.Photo)
                image_object.image = rent_object.Photo
                if rent_object.Status == 1:
                    Label(obj_frame, text=rent_object.Name).pack()
                    btn = Button(obj_frame, text="Подробнее", fg="white", bg="black")
                    btn.bind("<ButtonPress-1>", lambda event, arg=rent_object: self.open_details_info(arg))
                    btn.pack()
                else:
                    image_object.config(background="gray")
                    Label(obj_frame, text=rent_object.Name, background="gray", foreground="white").pack()
                    Label(obj_frame, text="Ожидает подтверждения", background="gray", foreground="white").pack()
                    obj_frame.config(background="gray")
                    btn = Button(obj_frame, text="Отменить аренду")
                    btn.bind("<ButtonPress-1>", lambda event, arg=rent_object.Id: self.cancellation_rent(arg))
                    btn.pack()

                obj_frame.grid(row=i, column=j, padx=5, pady=5)

                if index + 1 == count_object:
                    break

                index += 1

    def open_details_info(self, arg):
        details_info = Toplevel(self)
        details_info.title("Подробная информация")
        DetailsInfo(parent=details_info, object_dto=arg, resident_id=self.resident_id).pack()

    def cancellation_rent(self, object_id):
        if messagebox.askokcancel("Подтверждение", "Вы уверены?"):
            cancellation_rent(self.resident_id, object_id)

