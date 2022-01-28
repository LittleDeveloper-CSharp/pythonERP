from tkinter import Frame, Label


class RequestRentFrame(Frame):
    def __init__(self, master, object_rent):
        super().__init__(master)
        Label(self, image=object_rent.photo).grid(row=0, column=0)
        frame_description_info = Frame(self)
        Label(frame_description_info, text="Основная информация").pack()
        Label(frame_description_info, text=object_rent.RentPrice).pack()
        Label(frame_description_info, text=object_rent.Area).pack()
        Label(frame_description_info, text=f"{object_rent.DateStart} - {object_rent.DateEnd}").pack()
        Label(frame_description_info, text=object_rent.SumRent).pack()
        frame_description_info.grid(row=0, column=1)
