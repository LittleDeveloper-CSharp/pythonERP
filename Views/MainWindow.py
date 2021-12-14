from tkinter import Tk, Frame, Button, LEFT, Label, Toplevel

import Views.Partial.Resident.Menu

class Window(Tk):
    def __init__(self, role, id):
        super().__init__()

        self.title("Плитка резидента")

        frame_menu = Frame()

        if role == 2:
            Views.Partial.Resident.Menu.Menu(self, frame_menu, id)

        frame_menu.grid(row=0, column=0)

        frame_content = Frame()

        frame_content.grid(row=1, column=0)
