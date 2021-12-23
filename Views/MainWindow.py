from tkinter import Tk, Frame

import Views.Partial.Resident.ResidentMenu


class Window(Tk):
    def __init__(self, user):
        super().__init__()

        frame_menu = Frame()

        if user[0][1] == 2:
            self.title("Плитка резидента")
            Views.Partial.Resident.ResidentMenu.ResidentMenu(frame_menu, user[1][0])
        elif user[0][1] == 1:
            self.title("Плитка управляющего")
            Views.Partial.Resident.ResidentMenu.ResidentMenu(frame_menu, user[1][0])
        else:
            self.title("Плитка бухгалтера")
        frame_menu.grid(row=0, column=0)
