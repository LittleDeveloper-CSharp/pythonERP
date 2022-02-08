from tkinter import Frame, Button, LEFT, RIGHT, messagebox

from Models.resident_object import get_details_info
from Views.Pagination.PaginationItem.object_item import ObjectPartial
from Views.Pagination.pagination_list import PaginationList
from Views.Pagination.PaginationItem.resident_object_item import ResidentObjectPartial
from Service.ORM.available_object import get_available_object
from Service.ORM.resident_object import get_resident_object
from Views.Partial.Resident.Content.docs_frame import DocsFrame
from Views.Partial.Resident.Content.profile import Profile


class ResidentMenu:
    def __init__(self, main_frame, user):
        self.resident = user.resident
        self.master = main_frame
        self.content = Frame(main_frame)
        frame_menu = Frame(main_frame)

        is_active_acc = get_details_info(self.resident.Id)

        frame_menu.grid(row=0, column=0)
        self.content.grid(row=1, column=0)

        if is_active_acc is not None:

            Button(frame_menu, text="Главная", command=self.resident_objects).pack(side=LEFT)

            Button(frame_menu, text="Доступные помещения", command=self.free_object).pack(side=LEFT)

        Button(frame_menu, text="Профиль", command=self.profile_resident).pack(side=LEFT)

        if is_active_acc is not None:

            Button(frame_menu, text="Документы", command=self.docs_frame).pack(side=LEFT)

            self.resident_objects()
        else:
            self.profile_resident()
            messagebox.showinfo("Ошибка", "Вы не заполнили дополнительную информацию об аккаунте, "
                                          "как заполните, перезайдите в приложение")

        Button(frame_menu, text="Выход", command=self.exit_profile).pack(side=LEFT)

    def destroy_widget(self):
        for item in self.content.winfo_children():
            item.destroy()

    def profile_resident(self):
        self.destroy_widget()
        Profile(self.content, self.resident.Id, True, self.profile_resident).grid(row=1, column=0)

    def free_object(self):
        self.destroy_widget()
        free_object = [ObjectPartial(i, self.resident, self.free_object) for i in get_available_object()]
        PaginationList(self.content, free_object).grid(row=1, column=0)
        self.create_pagination_width()

    def resident_objects(self):
        self.destroy_widget()
        rent_object = [ResidentObjectPartial(i, self.resident, self.resident_objects)
                       for i in get_resident_object(self.resident.Id)]
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

    def exit_profile(self):
        self.master.master.destroy()
        from Views.Common.authorization_window import AuthWindow
        AuthWindow().mainloop()
