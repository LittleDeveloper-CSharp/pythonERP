from tkinter import *
from tkinter import messagebox

from DTO.resident import Resident
from Models.authorization_model import authorization_user
from Views.Partial.Resident.Content.edit_profile_resident import EditProfileResidentFrame
from Views.Partial.Resident.Content.profile import Profile


class AuthWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title("Авторизация")

        main_frame = Frame(self)

        Label(main_frame, text="Логин").pack()
        self.loginText = Entry(main_frame)
        self.loginText.pack()

        Label(main_frame, text="Пароль").pack()
        self.passwordText = Entry(main_frame)
        self.passwordText.pack()

        Button(main_frame, text="Вход", foreground="white", bg="black", borderwidth=0,
               command=self.authorization).pack(pady=5)

        Button(main_frame, text="Регистрация", command=self._regi).pack()

        main_frame.pack(pady=10, padx=60)

    def authorization(self):
        user = authorization_user(self.loginText.get(), self.passwordText.get())
        if user is not None:
            if user.isActive == 0:
                messagebox.showinfo("Ошибка", "Пользователь не активен")
                return
            self.destroy()
            from Views.Common.main_window import Window
            Window(user).mainloop()
        else:
            messagebox.showinfo("Ошибка", "Неправильный логин или пароль")

    def _regi(self):
        create_user = Toplevel(self)
        EditProfileResidentFrame(create_user, Resident()).pack()
        create_user.grab_set()


root = AuthWindow()
root.mainloop()
