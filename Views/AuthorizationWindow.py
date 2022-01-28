from tkinter import *
from tkinter import messagebox

from Views.MainWindow import Window
from Models.authorization_model import authorization_user


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

        main_frame.pack(pady=10, padx=60)

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
