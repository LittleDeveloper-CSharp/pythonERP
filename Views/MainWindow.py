from tkinter import Tk, Frame

import Views.Partial.Resident.ResidentMenu


class Window(Tk):
    def __init__(self, user):
        super().__init__()

        main_frame = Frame(self)

        if user[0][1] == 2:
            self.title("Плитка резидента")
            Views.Partial.Resident.ResidentMenu.ResidentMenu(main_frame, user[1][0])
        elif user[0][1] == 1:
            self.title("Плитка управляющего")
            Views.Partial.Resident.ResidentMenu.ResidentMenu(main_frame, user[1][0])
        else:
            self.title("Плитка бухгалтера")

        main_frame.grid(padx=20)
