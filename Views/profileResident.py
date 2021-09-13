from tkinter import Frame, Button, Label

def GetProfileFrame():
    profile = Frame()
    Label(profile, text="Имя").pack()
    Label(profile, text="Фамилия").pack()
    Label(profile, text="Отчество").pack()
    Button(profile, text="Редактировать").pack()
    return profile
