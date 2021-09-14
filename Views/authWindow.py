from tkinter import *

def Authorization():
    root.destroy()
    import Views.mainWindow


root = Tk()

Label(text="Логин").pack()

loginText = Entry()
loginText.pack()

Label(text="Пароль").pack()

passwordText = Entry()
passwordText.pack()

Button(text="Авторизация", foreground="white", bg="black", borderwidth=0, command=Authorization).pack()

root.mainloop()
