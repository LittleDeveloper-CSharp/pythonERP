from tkinter import *
from tkinter import messagebox

from Views.mainWindow import Window
from Models.authModel import AuthorizationUser

def Authorization():
    idRole = AuthorizationUser(loginText.get(), passwordText.get())
    if idRole is not None:
        root.destroy()
        Window(idRole[0]).mainloop()
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
