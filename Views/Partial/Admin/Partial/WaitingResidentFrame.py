from tkinter import Frame, VERTICAL, END, LEFT, Button, RIGHT
from tkinter.ttk import Treeview, Scrollbar

from Models.admin_model import get_wait_rent, get_resident_for_update
from Service.Helper.WaitingResidentWidget.RequestForRent import RequestRentFrame
from Service.Helper.WaitingResidentWidget.RequestForUpdateFrame import RequestForUpdateFrame
from Service.ORM.wait_rent_object import RequestRentObject


class WaitingResident(Frame):
    def __init__(self, master, list_item):
        super().__init__(master)
        self.tree = Treeview(self, show="headings", columns=("#1", "#2", "#3"))
        self.tree.heading("#1", text="id")
        self.tree.heading("#2", text="Заявитель")
        self.tree.heading("#3", text="Тип заявки")
        ysb = Scrollbar(self, orient=VERTICAL, command=self.tree.yview)
        self.tree.config(yscrollcommand=ysb.set)
        self.tree.bind("<<TreeviewSelect>>", self.__select_item)
        self.list_item = list_item

        self.tree.grid(row=0, column=0)

        control_frame = Frame(self)

        self.content_solution = Frame(control_frame)

        self.content_solution.pack()

        button_solution = Frame(control_frame)

        Button(button_solution, text="Принять").pack(side=LEFT)
        Button(button_solution, text="Отклонить").pack(side=RIGHT)

        button_solution.pack()

        control_frame.grid(row=0, column=1)

        self.__fill_treeview()

    def __clear_content(self):
        for i in self.content_solution.winfo_children():
            i.destroy()

    def __fill_treeview(self):
        for i in self.list_item:
            self.tree.insert("", END, values=(i.Id, i.Name, i.Status))

    def __select_item(self, event):
        items = self.tree.selection()
        self.__clear_content()
        if items is not None:
            self.item = self.tree.item(items[0])["values"]
            if self.item[2] == "Ожидает изменения":
                RequestForUpdateFrame(self.content_solution, get_resident_for_update(self.item[0]))\
                    .grid(row=0, column=0)
            else:
                request_rent = RequestRentObject(get_wait_rent(self.item[0]))
                RequestRentFrame(self.content_solution, request_rent).grid(row=0, column=0)
