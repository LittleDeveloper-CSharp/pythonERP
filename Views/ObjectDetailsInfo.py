from tkinter import *
from tkinter import messagebox
from Models.ResidentObject import RentObject

class DetailsInfo(Frame):
    def open_personal(self):
        self.frame_info_personal = Frame(self)
        Label(self.frame_info_personal, text="Тут должен быть персонал, но мне лень").pack()
        self.frame_info_personal.grid(row=0, column=1)
        return

    def request_rent(self):
        RentObject(self.residentId, self.objectId)
        messagebox.showinfo("Успешно", "Запрос на аренду отправлен")
        self.parent.destroy()

    def __init__(self, parent, object):
        Frame.__init__(self, parent)
        self.parent = parent
        self.objectId = object.Id
        self.widgets(object)

    def widgets(self, object):
        self.frame_info = Frame(self)
        self.photo = Label(self.frame_info, image=object.Photo)
        self.label_name = Label(self.frame_info, text=object.Name)
        self.label_area = Label(self.frame_info, text=object.Area)

        self.photo.pack()
        self.label_name.pack()
        self.label_area.pack()

        if object.isActive == 1:
            self.bt_rent = Button(self.frame_info, text="Арендовать", command=self.request_rent)
        else:
            self.bt_rent = Button(self.frame_info, text="Персонал", command=self.open_personal)
        self.bt_rent.pack()

        self.frame_info.grid(row=0, column=0)
