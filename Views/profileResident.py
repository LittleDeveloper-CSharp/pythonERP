from Models.residentModel import GetDetailsInfo
from tkinter import Frame, Button, Label

def get_profile_frame(residentId):
    profile = Frame()
    residentTuple = GetDetailsInfo(residentId)
    Label(profile, image="").pack()
    Label(profile, text=f"Фамилия: {residentTuple[1]}").pack()
    Label(profile, text=f"Имя: {residentTuple[2]}").pack()
    Label(profile, text=f"Отчество: {residentTuple[3]}").pack()
    Label(profile, text=f"ИНН: {residentTuple[4]}").pack()
    Label(profile, text=f"Телефон: {residentTuple[5]}").pack()
    Label(profile, text=f"Email: {residentTuple[6]}").pack()
    Button(profile, text="Редактировать").pack()
    return profile
