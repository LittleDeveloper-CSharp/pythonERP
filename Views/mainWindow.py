import math
from tkinter import Tk, Frame, Button, LEFT, Label, Toplevel


from Views.detailseInfoObject import DetailsInfo
from Views.profileResident import get_profile_frame
from Views.ListResidentObject import get_resident_object
from Views.availableObject import get_available_object

class Window(Tk):
    def __init__(self, Id):
        super().__init__()

        frameMenu = Frame()

        self.residentId = Id

        self.title("Плитка резидента")

        frameMenu.grid(row=0, column=0)

        frameContent = Frame()

        frameContent.grid(row=1, column=0)

        Button(frameMenu, text="Главная", command=self.open_main_page).pack(side=LEFT)

        Button(frameMenu, text="Доступные помещения", command=self.open_available_object).pack(side=LEFT)

        Button(frameMenu, text="Профиль", command=self.open_profile_resident).pack(side=LEFT)

        self.open_main_page()

    def open_details_info(self, event, arg):
        details_info = Toplevel(self)
        details_info.title("Подробная информация")
        DetailsInfo(parent=details_info, object=arg, Id=self.residentId).pack()

    def create_frame_object(self, objects):
        frame_list_object = Frame(self)

        count_row = math.ceil(len(objects) / 10)
        count_object = len(objects)
        index = 0

        if count_object == 0:
            Label(frame_list_object, text="Информация отсутствует").pack()
            frame_list_object.grid(row=1, column=0)
            return

        for i in range(count_row):
            for j in range(10):
                objFrame = Frame(frame_list_object)

                imageObject = Label(objFrame)

                imageObject.pack()

                imageObject.config(image=objects[index].Photo)

                Label(objFrame, text=objects[index].Name).pack()

                btn = Button(objFrame, text="Подробнее", fg="white", bg="black")

                btn.bind("<ButtonPress-1>", lambda event, arg=objects[index]: self.open_details_info(event, arg))

                btn.pack()

                objFrame.grid(row=i, column=j)

                if index + 1 == count_object:
                    break

                index += 1

        frame_list_object.grid(row=1, column=0)

        self.mainloop()

    def clear_root(self):
        if self.winfo_children():
            self.winfo_children()[1].destroy()

    def open_profile_resident(self):
        self.clear_root()
        frameContent = get_profile_frame(self.residentId)
        frameContent.grid(row=1, column=0)

    def open_main_page(self):
        self.clear_root()
        self.create_frame_object(get_resident_object(self.residentId))

    def open_available_object(self):
        self.clear_root()
        self.create_frame_object(get_available_object())
