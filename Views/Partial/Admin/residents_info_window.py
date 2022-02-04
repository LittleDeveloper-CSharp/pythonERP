from tkinter import Frame, Label, Toplevel


class ResidentInfo(Frame):
    def __init__(self, master, resident_id):
        super().__init__(master)
        Label(master, text=resident_id).pack()
