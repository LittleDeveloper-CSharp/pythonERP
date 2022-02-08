from tkinter import Frame, Label, Button, Toplevel

from Models.admin_model import get_resident
from Views.Partial.Resident.Content.docs_frame import DocsFrame
from Views.Partial.Resident.Content.profile import Profile


class RequestRentFrame(Frame):
    def __init__(self, master, object_rent):
        super().__init__(master)
        self._object_rent = object_rent
        Label(self, image=object_rent.photo).grid(row=0, column=0)
        frame_description_info = Frame(self)
        Label(frame_description_info, text="Основная информация").pack()
        Label(frame_description_info, text=f"Площадь - {object_rent.area}").pack()
        Label(frame_description_info, text=f"Аренда - с {object_rent.date_start} - по {object_rent.date_end}").pack()
        Label(frame_description_info, text=f"Стоимость аренды - {object_rent.total_sum}").pack()
        Button(frame_description_info, text="Информация о Резиденте", command=self._open_resident_info).pack()
        frame_description_info.grid(row=0, column=1)

    def _open_resident_info(self):
        detail_info_resident = Toplevel()
        detail_info_resident.grab_set()
        Profile(detail_info_resident, self._object_rent.resident_id, False).grid(row=0, column=0)
        resident_login = get_resident(self._object_rent.resident_id)[1]
        DocsFrame(detail_info_resident, resident_login).grid(row=0, column=1)

