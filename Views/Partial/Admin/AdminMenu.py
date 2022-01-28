from tkinter import Frame, Button, LEFT

from DTO.request import RequestForRent, RequestForUpdate
from Models.admin_model import get_wait_rent_list, get_wait_update_list
from Service.Helper.ObjectItem import ObjectPartial
from Service.Helper.PaginataionList import PaginationList
from Service.Helper.ResidentItem import ResidentPartial
from Service.ORM.Objects import get_objects
from Service.ORM.ResidentsList import get_residents_list
from Views.Partial.Admin.Partial.WaitingResidentFrame import WaitingResident


class AdminMenu:
    def __init__(self, master):
        self.master = master
        frame_menu = Frame(master)
        self.content = Frame(master)
        Button(frame_menu, text="Объекты", command=self.object_list).pack(side=LEFT)

        Button(frame_menu, text="Резиденты", command=self.place_residents).pack(side=LEFT)

        Button(frame_menu, text="Комната ожидания", command=self.wait_resident).pack(side=LEFT)

        frame_menu.grid(row=0, column=0)

        self.content.grid(row=1, column=0)

        self.place_residents()

    def clear_content_frame(self):
        for item in self.content.winfo_children():
            item.destroy()

    def place_residents(self):
        self.clear_content_frame()
        residents = get_residents_list()
        PaginationList(self.content, [ResidentPartial(i) for i in residents]).grid(row=1, column=0)

    def object_list(self):
        self.clear_content_frame()
        objects = get_objects()
        PaginationList(self.content, [ObjectPartial(i) for i in objects]).grid(row=1, column=0)

    def wait_resident(self):
        self.clear_content_frame()
        request = (*[RequestForRent(i) for i in get_wait_rent_list()],
                   *[RequestForUpdate(i) for i in get_wait_update_list()])
        WaitingResident(self.content, request).grid(row=1, column=0)

