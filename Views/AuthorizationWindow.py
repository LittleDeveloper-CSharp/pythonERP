from tkinter import *
from tkinter import messagebox

from Views.MainWindow import Window
from Models.AuthorizationModel import authorization_user


class AuthWindow(Tk):
    def __init__(self):
        super().__init__()

        Label(text="Логин").pack()
        self.loginText = Entry()
        self.loginText.pack()

        Label(text="Пароль").pack()
        self.passwordText = Entry()
        self.passwordText.pack()

        Button(text="Авторизация", foreground="white", bg="black", borderwidth=0, command=self.authorization).pack()

    def authorization(self):
        user = authorization_user(self.loginText.get(), self.passwordText.get())
        if user is not None:
            root.destroy()
            Window(user).mainloop()
        else:
            messagebox.showinfo("Ошибка", "Неправильный логин или пароль")


if __name__ == '__main__':
    root = AuthWindow()
    root.mainloop()
