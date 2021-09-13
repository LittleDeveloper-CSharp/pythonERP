from tkinter import Toplevel, Frame, Button, Label
from PIL import Image, ImageTk

def OpenDetailsInfo(event, arg):
    detailsInfo = Toplevel()
    detailsInfo.title("Подробная информация")
    Label(detailsInfo, text=arg).pack()

def GetResidentObject():
    frameContent = Frame()
    sourcePhoto = Image.open('./Controllers/image/2.jpg')
    photo = sourcePhoto.resize((200, 200))

    photoTK = ImageTk.PhotoImage(photo)

    for i in range(2):
        for j in range(4):
            objFrame = Frame(frameContent)

            Label(objFrame, image=photoTK).pack()

            Label(objFrame, text="Объект 1").pack()

            btn = Button(objFrame, text="Подробнее", fg="white", bg="black")

            btn.bind('<ButtonPress-1>', lambda event, arg=(i+1)+j: OpenDetailsInfo(event, arg))

            btn.pack()

            objFrame.grid(row=i, column=j)

    return frameContent

