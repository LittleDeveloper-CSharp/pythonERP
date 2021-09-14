from tkinter import Frame, Button, Label

def get_profile_frame():
    profile = Frame()
    Label(profile, text="Имя").pack()
    Label(profile, text="Фамилия").pack()
    Label(profile, text="Отчество").pack()
    Button(profile, text="Редактировать").pack()
    return profile
