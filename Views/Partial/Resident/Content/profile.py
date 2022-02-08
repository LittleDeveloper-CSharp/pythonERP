from tkinter import Label, Button, Frame, Toplevel

from DTO.resident import Resident
from Models.object_market_place_model import get_details_info
from Service.opener_photo import set_photo
from Views.Partial.Resident.Content.ProfileDetailsInfo import ProfileDetailsInfo
from Views.Partial.Resident.Content.edit_profile_resident import EditProfileResidentFrame


class Profile(Frame):
    def __init__(self, master, resident_id, is_resident, refresh_frame=None):
        super().__init__(master)
        self.delegate_refresh_frame = refresh_frame
        resident = Resident().set_value(get_details_info(resident_id))
        photo_path = resident.photo_path
        self.is_resident = is_resident

        image = set_photo(photo_path)
        panel = Label(self)
        panel.grid(row=0, column=0)
        panel.configure(image=image)
        panel.image = image

        frame_information = Frame(self)
        Label(frame_information, text=f"Логин: {resident.login}").pack()
        Label(frame_information, text=f"Фамилия: {resident.last_name}").pack()
        Label(frame_information, text=f"Имя: {resident.first_name}").pack()
        Label(frame_information, text=f"Отчество: {resident.patronymic}").pack()
        Label(frame_information, text=f"ИНН: {resident.inn}").pack()
        Label(frame_information, text=f"Телефон: {resident.phone}").pack()
        Label(frame_information, text=f"Email: {resident.email}").pack()
        if refresh_frame is not None:
            Button(frame_information, text="Редактировать", command=lambda: self.__edit_profile_click(resident)).pack()

        Button(frame_information, text="Подробная информация",
               command=lambda: self.__open_details_profile(resident_id)).pack()
        frame_information.grid(row=0, column=1)

    def __edit_profile_click(self, resident):
        edit_modal = Toplevel(self)
        EditProfileResidentFrame(edit_modal, resident, self.is_resident, self.delegate_refresh_frame).pack()
        edit_modal.title("Редактирование")

    def __open_details_profile(self, resident_id):
        detail_info = Toplevel(self)
        ProfileDetailsInfo(detail_info, resident_id, self.is_resident).pack()
        detail_info.title("Подробная информация")
