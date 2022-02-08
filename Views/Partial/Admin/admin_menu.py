from tkinter import Frame, Button, LEFT

from DTO.object_market_place import ObjectModel
from DTO.request import RequestForRent, RequestForUpdate
from Models.admin_model import get_wait_rent_list, get_wait_update_list
from Views.Pagination.PaginationItem.object_item import ObjectPartial
from Views.Pagination.pagination_list import PaginationList
from Views.Pagination.PaginationItem.resident_item import ResidentPartial
from Service.ORM.objects import get_objects
from Service.ORM.residents_list import get_residents_list
from Views.Partial.Admin.Partial.report_frame import ReportFrame
from Views.Partial.Admin.Partial.waiting_resident_frame import WaitingResident


class AdminMenu:
    def __init__(self, master):
        self.master = master
        frame_menu = Frame(master)
        self.content = Frame(master)
        Button(frame_menu, text="Объекты", command=self.object_list).pack(side=LEFT)

        Button(frame_menu, text="Резиденты", command=self.place_residents).pack(side=LEFT)

        Button(frame_menu, text="Комната ожидания", command=self.wait_resident).pack(side=LEFT)

        Button(frame_menu, text="Отчеты", command=self.report).pack(side=LEFT)

        Button(frame_menu, text="Выход", command=self.exit_profile).pack(side=LEFT)

        frame_menu.grid(row=0, column=0)

        self.content.grid(row=1, column=0)

        self.place_residents()

    def report(self):
        self.clear_content_frame()
        ReportFrame(self.content).grid(row=1, column=0)

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
        new_object = ObjectModel()
        new_object.Id = None
        new_object.Name = "Добавить"
        new_object.photo_path = "../Resources/image/znak-plius.png"

        pagination_item = [ObjectPartial(i, delegate_refresh=self.object_list) for i in objects]
        pagination_item.insert(0, ObjectPartial(new_object, delegate_refresh=self.object_list))
        PaginationList(self.content, pagination_item).grid(row=1, column=0)

    def wait_resident(self):
        self.clear_content_frame()
        request = (*[RequestForRent(i) for i in get_wait_rent_list()],
                   *[RequestForUpdate(i) for i in get_wait_update_list()])
        WaitingResident(self.content, request, self.wait_resident).grid(row=1, column=0)

    def exit_profile(self):
        self.master.master.destroy()
        from Views.Common.authorization_window import AuthWindow
        AuthWindow().mainloop()
