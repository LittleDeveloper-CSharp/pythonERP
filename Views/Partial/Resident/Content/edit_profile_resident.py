from tkinter import Frame, Entry, Label, Button, filedialog

from Models.resident_object import edit_profile

from Service.copy_file import copy_file
from Service.dir import create_doc_dir
from Service.opener_photo import set_photo


class EditProfileResidentFrame(Frame):
    def __init__(self, parent, resident, refresh_frame=None):
        Frame.__init__(self, parent)
        self.resident = resident
        self.parent = parent
        self.file_path = None

        self.delegate_refresh_frame = refresh_frame

        frame_info = Frame(self)

        if resident.Id == 0:
            frame_login = Frame(frame_info)
            Label(frame_login, text="Логин").grid(row=0, column=0)
            self.entry_login = Entry(frame_login)
            self.entry_login.grid(row=0, column=1)
            frame_login.pack()

        frame_last_name = Frame(frame_info)
        Label(frame_last_name, text="Отчество").grid(row=0, column=0)
        self.entry_last_name = Entry(frame_last_name)
        self.entry_last_name.grid(row=0, column=1)
        frame_last_name.pack()

        frame_first_name = Frame(frame_info)
        Label(frame_first_name, text="Имя").grid(row=0, column=0)
        self.entry_first_name = Entry(frame_first_name)
        self.entry_first_name.grid(row=0, column=1)
        frame_first_name.pack()

        frame_patronymic = Frame(frame_info)
        Label(frame_patronymic, text="Фамилия").grid(row=0, column=0)
        self.entry_patronymic = Entry(frame_patronymic)
        self.entry_patronymic.grid(row=0, column=1)
        frame_patronymic.pack()

        frame_inn = Frame(frame_info)
        Label(frame_inn, text="ИНН").grid(row=0, column=0)
        self.entry_inn = Entry(frame_inn)
        self.entry_inn.grid(row=0, column=1)
        frame_inn.pack()

        frame_phone = Frame(frame_info)
        Label(frame_phone, text="Телефон").grid(row=0, column=0)
        self.entry_phone = Entry(frame_phone)
        self.entry_phone.grid(row=0, column=1)
        frame_phone.pack()

        frame_email = Frame(frame_info)
        Label(frame_email, text="Email").grid(row=0, column=0)
        self.entry_email = Entry(frame_email)
        self.entry_email.grid(row=0, column=1)
        frame_email.pack()

        frame_password = Frame(frame_info)
        Label(frame_password, text="Пароль").grid(row=0, column=0)
        self.entry_password = Entry(frame_password)
        self.entry_password.grid(row=0, column=1)
        frame_password.pack()

        frame_info.grid(row=0, column=1)

        Button(frame_info, text="Принять изменения", command=self.__accept_edit).pack()

        frame_photo = Frame(self)

        if resident.Id != 0:
            self.__fill_entry()

        image = set_photo(resident.photo_path)
        self.panel = Label(frame_photo)
        self.panel.pack()
        self.panel.configure(image=image)
        self.panel.image = image
        Button(frame_photo, text="Изменить фото", command=self.__ask_open_photo).pack()

        frame_photo.grid(row=0, column=0)

    def __fill_entry(self):
        self.entry_phone.insert(0, self.resident.phone)
        self.entry_email.insert(0, self.resident.email)
        self.entry_inn.insert(0, self.resident.inn)
        self.entry_patronymic.insert(0, self.resident.patronymic)
        self.entry_last_name.insert(0, self.resident.last_name)
        self.entry_first_name.insert(0, self.resident.first_name)

    def __accept_edit(self):
        if self.resident.Id == 0:
            self.resident.login = self.entry_login.get()

        self.resident.phone = self.entry_phone.get()
        self.resident.email = self.entry_email.get()
        self.resident.inn = self.entry_inn.get()
        self.resident.patronymic = self.entry_patronymic.get()
        self.resident.last_name = self.entry_last_name.get()
        self.resident.first_name = self.entry_first_name.get()

        if self.resident.Id == 0:
            create_doc_dir(self.resident.login)

        if self.file_path is not None:
            file_name = f'{self.resident.first_name + self.resident.last_name}.{self.file_path.split(".")[1]}'
            self.resident.photo_path = f"../Resources/image/{file_name}"
            copy_file(self.file_path, "../Resources/image/", file_name)

        edit_profile(self.resident, self.entry_password.get())
        if self.delegate_refresh_frame is not None:
            self.delegate_refresh_frame()
        self.parent.destroy()

    def __ask_open_photo(self):
        self.file_path = filedialog.askopenfilename()

        image = set_photo(self.file_path)
        self.panel.configure(image=image)
        self.panel.image = image
