from tkinter import Frame, Label, Button, Toplevel
import math

from Views.ObjectDetailsInfo import DetailsInfo


class ListObject:
    def __init__(self, objects):
        frame_list = Frame()

        count_row = math.ceil(len(objects) / 10)
        count_object = len(objects)
        index = 0

        if count_object == 0:
            Label(self, text="Информация отсутствует").pack()
            return

        for i in range(count_row):
            for j in range(10):
                obj_frame = Frame(frame_list)

                image_object = Label(obj_frame)

                image_object.pack()

                image_object.config(image=objects[index].Photo)

                Label(obj_frame, text=objects[index].Name).pack()

                btn = Button(obj_frame, text="Подробнее", fg="white", bg="black")

                btn.bind("<ButtonPress-1>", lambda event, arg=objects[index]: self.open_details_info(event, arg))

                btn.pack()

                obj_frame.grid(row=i, column=j)

                if index + 1 == count_object:
                    break

                index += 1

    def open_details_info(self, event, arg):
        details_info = Toplevel(self)
        details_info.title("Подробная информация")
        DetailsInfo(parent=details_info, object=arg).pack()
