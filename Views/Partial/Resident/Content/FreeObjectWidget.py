from tkinter import Frame, Label, Button, Toplevel
import math

from DTO.objectDTO import ObjectModel
from Views.ObjectDetailsInfo import DetailsInfo
from Models.ObjectModel import get_free_object


class FreeObject(Frame):
    def __init__(self, master, resident_id, refresh_frame):
        super().__init__(master)

        objects_tuple = get_free_object()

        self.delegate_refresh_frame = refresh_frame

        objects = [ObjectModel(i) for i in objects_tuple]

        count_row = math.ceil(len(objects) / 10)
        count_object = len(objects)
        index = 0

        if count_object == 0:
            Label(self, text="Информация отсутствует").pack()
            return

        for i in range(count_row):
            for j in range(10):
                obj_frame = Frame(self)
                free_object = objects[index]
                image_object = Label(obj_frame)

                image_object.pack()
                image_object.config(image=free_object.Photo)

                Label(obj_frame, text=free_object.Name).pack()

                btn = Button(obj_frame, text="Подробнее", fg="white", bg="black")
                btn.bind("<ButtonPress-1>", lambda event, arg=free_object: self.open_details_info(arg, resident_id))
                btn.pack()

                obj_frame.grid(row=i, column=j, padx=5, pady=5)

                if index + 1 == count_object:
                    break

                index += 1

    def open_details_info(self, arg, resident_id):
        details_info = Toplevel(self)
        details_info.title("Подробная информация")
        DetailsInfo(parent=details_info, object_dto=arg, resident_id=resident_id,
                    refresh_frame=self.delegate_refresh_frame).pack()
