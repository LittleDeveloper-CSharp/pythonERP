import datetime
from tkinter import *
from tkinter import messagebox
from Models.ResidentObject import resident_objects
from tkcalendar import Calendar


class DetailsInfo(Frame):
    def __init__(self, parent, object_dto, resident_id):
        Frame.__init__(self, parent)
        self.parent = parent
        self.frame_info = Frame(self)
        if object_dto.isActive == 1:
            self.frame_first_step_rent = Frame(self)
            self.frame_second_step_rent = Frame(self)
            self.resident_id = resident_id
            self.btn = Button(self.frame_info, text="Арендовать", command=self.select_start_date)

            date = datetime.date.today()
            Label(self.frame_first_step_rent, text="Начало аренды").pack()
            self.calStart = Calendar(master=self.frame_first_step_rent, year=date.year, month=date.month, day=date.day,
                                     mindate=date, locale="ru_RU")
            Label(self.frame_second_step_rent, text="Конец аренды").pack()
            self.calEnd = Calendar(master=self.frame_second_step_rent, locale="ru_RU")
            self.calEnd.pack()
            Button(self.frame_second_step_rent, text="Подтвердить", command=self.request_rent).pack()
            self.calStart.pack()
        else:
            self.btn = Button(self.frame_info, text="Персонал", command=self.open_personal)
            self.frame_info_personal = Frame(self)

        self.frame_description_info = Frame(self)

        self.objectId = object_dto.Id

        self.widgets(object_dto)

    def select_start_date(self):
        self.btn.pack_forget()
        self.frame_first_step_rent.grid(row=0, column=2)

    def select_end_date(self):
        self.frame_first_step_rent.destroy()
        date_tuple = self.calStart.get_date().split('.')
        date = datetime.date(year=int(date_tuple[2]), month=int(date_tuple[1]), day=int(date_tuple[0]))
        self.calEnd.config(mindate=date)
        self.frame_second_step_rent.grid(row=0, column=2)

    def widgets(self, free_object):
        Label(self.frame_info, image=free_object.Photo).pack()
        Label(self.frame_info, text=free_object.Name).pack()

        Label(self.frame_description_info, text="Основная информация").pack()
        Label(self.frame_description_info, text=free_object.rentPrice).pack()
        Label(self.frame_description_info, text=free_object.Area).pack()
        Label(self.frame_description_info, text=free_object.isActive).pack()

        if free_object.isActive == 1:
            Button(self.frame_first_step_rent, text="Выбрать", command=self.select_end_date).pack()
        self.btn.pack()

        self.frame_info.grid(row=0, column=0)
        self.frame_description_info.grid(row=0, column=1)

    def open_personal(self):
        Label(self.frame_info_personal, text="Тут должен быть персонал, но мне лень").pack()
        self.frame_info_personal.grid(row=0, column=1)
        return

    def request_rent(self):
        resident_objects(self.resident_id, self.objectId, self.calStart.get_date(), self.calEnd.get_date())
        messagebox.showinfo("Успешно", "Запрос на аренду отправлен")
        self.parent.destroy()
