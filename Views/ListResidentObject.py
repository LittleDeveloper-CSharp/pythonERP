from tkinter import Tk, Frame, Button, LEFT, Label
from PIL import Image, ImageTk

def GetResidentObject():
    frameContent = Frame()
    sourcePhoto = Image.open('./Controllers/image/2.jpg')
    photo = sourcePhoto.resize((200, 200))

    photoTK = ImageTk.PhotoImage(photo)

    for i in range(2):
        for j in range(4):
            objFrame = Frame(frameContent)

            imageObject = Label(objFrame, image=photoTK)

            imageObject.pack()

            Label(objFrame, text="Объект 1").pack()

            Button(objFrame, text="Подробнее", fg="white", bg="black").pack()

            objFrame.grid(row=i, column=j)

    return frameContent
