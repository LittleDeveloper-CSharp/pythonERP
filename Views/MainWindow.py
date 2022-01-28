from tkinter import Tk, Frame

from Views.Partial.Resident.ResidentMenu import ResidentMenu
from Views.Partial.Admin.AdminMenu import AdminMenu


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
