from tkinter import Frame, Entry, Label, Button, filedialog
from Models.ResidentObject import edit_profile
from shutil import copyfile


class EditProfileResidentFrame(Frame):
    def __init__(self, parent, resident, refresh_frame):
        Frame.__init__(self, parent)
        self.resident = resident
        self.parent = parent

        self.delegate_refresh_frame = refresh_frame

        frame_info = Frame(self)

        # frame_login = Frame(frame_info)
        # Label(frame_login, text="Логин").grid(row=0, column=0)
        # self.entry_login = Entry(frame_login)
        # self.entry_login.grid(row=0, column=1)
        # frame_login.pack()

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

        image = self.__set_photo()

        frame_photo = Frame(self)
        self.panel = Label(frame_photo)
        self.panel.pack()
        self.panel.configure(image=image)
        self.panel.image = image
        Button(frame_photo, text="Изменить фото", command=self.__ask_open_photo).pack()

        frame_photo.grid(row=0, column=0)

        self.__fill_entry()

    def __fill_entry(self):
        self.entry_phone.insert(0, self.resident.phone)
        self.entry_email.insert(0, self.resident.email)
        self.entry_inn.insert(0, self.resident.inn)
        # self.entry_login.insert(0, self.resident.login)
        self.entry_patronymic.insert(0, self.resident.patronymic)
        self.entry_last_name.insert(0, self.resident.last_name)
        self.entry_first_name.insert(0, self.resident.first_name)

    def __accept_edit(self):
        self.resident.phone = self.entry_phone.get()
        self.resident.email = self.entry_email.get()
        self.resident.inn = self.entry_inn.get()
        # self.resident.login = self.entry_login.get()
        self.resident.patronymic = self.entry_patronymic.get()
        self.resident.last_name = self.entry_last_name.get()
        self.resident.first_name = self.entry_first_name.get()

        edit_profile(self.resident, self.entry_password.get())
        self.delegate_refresh_frame()
        self.parent.destroy()

    def __ask_open_photo(self):
        self.resident.photo_path = filedialog.askopenfilename()

        new_photo_path = f'../Resources/image/{self.resident.first_name+self.resident.last_name}.' \
                         f'{self.resident.photo_path.split(".")[1]}'

        copyfile(self.resident.photo_path, new_photo_path)
        self.resident.photo_path = new_photo_path
        image = self.__set_photo()
        self.panel.configure(image=image)
        self.panel.image = image

    def __set_photo(self):
        import os
        from PIL import Image, ImageTk
        photo_path = self.resident.photo_path

        if photo_path is None:
            photo_path = '../Resources/image/emptyPeople.png'

        path = os.path.abspath(photo_path)

        source_photo = Image.open(path)
        photo = source_photo.resize((200, 200))
        image = ImageTk.PhotoImage(photo)
        return image
