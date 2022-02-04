from tkinter import Frame, VERTICAL, END, LEFT, Button, RIGHT
from tkinter.ttk import Treeview, Scrollbar

from DTO.resident import Resident
from Models.admin_model import get_resident_for_update, update_property_rent, accept_update_resident, \
    get_request_by_rent
from Views.Partial.Admin.Partial.WaitingResidentWidget.request_for_rent import RequestRentFrame
from Views.Partial.Admin.Partial.WaitingResidentWidget.request_for_update_frame import RequestForUpdateFrame
from DTO.request_rent_object import RequestRentObject


class WaitingResident(Frame):
    def __init__(self, master, list_item, delegate_update_main):
        super().__init__(master)
        self.delegate_update_main = delegate_update_main
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

        self.content_solution.pack(padx=(25, 0))

        button_solution = Frame(control_frame)

        self.accept_button = Button(button_solution, text="Принять")
        self.canceller_button = Button(button_solution, text="Отклонить")

        self.accept_button.pack(side=LEFT)
        self.canceller_button.pack(side=RIGHT)

        button_solution.pack(padx=(25, 0))

        control_frame.grid(row=0, column=1)

        self.__fill_treeview()

    def __clear_content(self):
        for i in self.content_solution.winfo_children():
            i.destroy()

    def __fill_treeview(self):
        for i in self.list_item:
            self.tree.insert("", END, values=(i.Id, i.Name or "Новый пользователь", i.Status))

    def __select_item(self, event):
        items = self.tree.selection()
        self.__clear_content()
        if items is not None:
            self.item = self.tree.item(items[0])["values"]
            if self.item[2] == "Ожидает изменения":
                resident_for_update = get_resident_for_update(self.item[0])
                RequestForUpdateFrame(self.content_solution, resident_for_update) \
                    .grid(row=0, column=0)

                self.accept_button.config(command=lambda: self.button_click(command=lambda: accept_update_resident
                                                                            (Resident()
                                                                             .set_value(resident_for_update[1]), 1)))
                self.canceller_button.config(command=lambda: self.button_click(command=lambda: accept_update_resident
                                                                               (Resident()
                                                                                .set_value(resident_for_update[1]), 0)))
            else:
                request_rent = RequestRentObject(get_request_by_rent(self.item[0]))
                RequestRentFrame(self.content_solution, request_rent).grid(row=0, column=0)

                self.accept_button.config(command=lambda: self.button_click(command=lambda: update_property_rent(
                    request_rent.id, 1)))
                self.canceller_button.config(command=lambda: self.button_click(command=lambda: update_property_rent
                                                                               (request_rent.id, 3)))

    def button_click(self, command):
        command()
        self.delegate_update_main()
