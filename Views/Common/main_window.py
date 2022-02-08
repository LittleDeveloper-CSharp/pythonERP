from tkinter import Frame, Tk

from Views.Partial.Resident.resident_menu import ResidentMenu
from Views.Partial.Admin.admin_menu import AdminMenu


class Window(Tk):
    def __init__(self, user):
        super().__init__()

        main_frame = Frame(self)

        if user.idRole == 2:
            self.title("Плитка резидента")
            ResidentMenu(main_frame, user)
        elif user.idRole == 1:
            self.title("Плитка управляющего")
            AdminMenu(main_frame)
        else:
            self.title("Плитка бухгалтера")

        main_frame.grid(padx=20)
