from tkinter import *
from tkinter import messagebox

from Views.MainWindow import Window
from Models.AuthorizationModel import AuthorizationUser

def Authorization():
    role_id, resident_id = AuthorizationUser(loginText.get(), passwordText.get())
    if role_id is not None:
        root.destroy()
        Window(role_id, resident_id).mainloop()
    else:
        messagebox.showinfo("Ошибка", "Не правильный логин или пароль")


root = Tk()

Label(text="Логин").pack()

loginText = Entry()
loginText.pack()

Label(text="Пароль").pack()

passwordText = Entry()
passwordText.pack()

Button(text="Авторизация", foreground="white", bg="black", borderwidth=0, command=Authorization).pack()

root.mainloop()
