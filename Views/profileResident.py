from tkinter import Tk, Frame, Button, LEFT, Label
from PIL import Image, ImageTk

def GetProfileFrame():
    profile = Frame()
    Label(profile, text="Имя").pack()
    Label(profile, text="Фамилия").pack()
    Label(profile, text="Отчество").pack()
    return profile
