from tkinter import Frame, Button, LEFT, RIGHT

from Models.object_market_place_model import get_free_object
from Service.Helper.ObjectItem import ObjectPartial
from Service.Helper.PaginataionList import PaginationList
from Service.Helper.ResidentItem import ResidentPartial
from Service.Helper.ResidentObjectItem import ResidentObjectPartial
from Service.ORM.AvailableObject import get_available_object
from Service.ORM.ResidentObject import get_resident_object
from Views.Partial.Resident.Content.DocsFrame import DocsFrame
from Views.Partial.Resident.Content.ProfileWidget import Profile
from Models.resident_object import get_rent_object


class ResidentMenu:
    def __init__(self, main_frame, user):
        self.resident = user.resident
        self.content = Frame(main_frame)
        frame_menu = Frame(main_frame)

        Button(frame_menu, text="Главная", command=self.resident_objects).pack(side=LEFT)

        Button(frame_menu, text="Доступные помещения", command=self.free_object).pack(side=LEFT)

        Button(frame_menu, text="Профиль", command=self.profile_resident).pack(side=LEFT)

        Button(frame_menu, text="Документы", command=self.docs_frame).pack(side=LEFT)

        frame_menu.grid(row=0, column=0)
        self.content.grid(row=1, column=0)

        self.resident_objects()

    def destroy_widget(self):
        for item in self.content.winfo_children():
            item.destroy()

    def profile_resident(self):
        self.destroy_widget()
        Profile(self.content, self.resident.Id, self.profile_resident).grid(row=1, column=0)

    def free_object(self):
        self.destroy_widget()
        free_object = [ObjectPartial(i) for i in get_available_object()]
        PaginationList(self.content, free_object).grid(row=1, column=0)
        self.create_pagination_width()

    def resident_objects(self):
        self.destroy_widget()
        rent_object = [ResidentObjectPartial(i) for i in get_resident_object(self.resident.Id)]
        PaginationList(self.content, rent_object).grid(row=1, column=0)
        self.create_pagination_width()

    def docs_frame(self):
        self.destroy_widget()
        DocsFrame(self.content, self.resident.login).grid(row=1, column=0)

    def create_pagination_width(self):
        if len(self.content.children) > 5:
            frame_size_panel = Frame(self.content)
            Button(frame_size_panel, text="5").pack(side=LEFT)
            Button(frame_size_panel, text="10").pack(side=LEFT)
            Button(frame_size_panel, text="15").pack(side=LEFT)
            frame_size_panel.grid(row=0, column=0)

            frame_pagination = Frame(self.content)
            Button(frame_pagination, text="<<").pack(side=LEFT)
            Button(frame_pagination, text=">>").pack(side=RIGHT)
            frame_pagination.grid(row=2, column=0)
