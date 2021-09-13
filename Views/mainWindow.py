import math
from tkinter import Tk, Frame, Button, LEFT, Label, Toplevel

from PIL import Image, ImageTk

from Views.profileResident import GetProfileFrame
from Views.ListResidentObject import GetResidentObject
from Views.availableObject import GetAvailableObject

def OpenDetailsInfo(event, arg):
    detailsInfo = Toplevel()
    detailsInfo.title("Подробная информация")
    Label(detailsInfo, text=arg).pack()

def CreateFrameObject(objects):
    global mainRoot
    import os

    frameListObject = Frame(mainRoot)

    countRow = math.ceil(len(objects) / 10)
    countObject = len(objects)
    index = 0
    for i in range(countRow):
        for j in range(10):
            path = os.path.abspath(f"{objects[index].PhotoPath}")
            sourcePhoto = Image.open(path)

            photo = sourcePhoto.resize((200, 200))

            photoTK = ImageTk.PhotoImage(photo)

            objFrame = Frame(frameListObject)

            imageObject = Label(objFrame)

            imageObject.pack()

            imageObject.config(image=photoTK)

            Label(objFrame, text=objects[index].Name).pack()

            btn = Button(objFrame, text="Подробнее", fg="white", bg="black")

            btn.bind("<ButtonPress-1>", lambda event, arg=objects[index].Id: OpenDetailsInfo(event, arg))

            btn.pack()

            objFrame.grid(row=i, column=j)

            if index + 1 == countObject:
                break

            index += 1

    frameListObject.grid(row=1, column=0)

    mainRoot.mainloop()

def ClearRoot():
    if mainRoot.winfo_children():
        mainRoot.winfo_children()[1].destroy()

def OpenProfileResident():
    global frameContent
    ClearRoot()
    frameContent = GetProfileFrame()
    frameContent.grid(row=1, column=0)

def OpenMainPage():
    ClearRoot()
    CreateFrameObject(GetAvailableObject())


def OpenAvailableObject():
    ClearRoot()
    CreateFrameObject(GetAvailableObject())


mainRoot = Tk()

frameMenu = Frame()

frameMenu.grid(row=0, column=0)

frameContent = Frame()

frameContent.grid(row=1, column=0)

Button(frameMenu, text="Главная", command=OpenMainPage).pack(side=LEFT)

Button(frameMenu, text="Доступные помещения", command=OpenAvailableObject).pack(side=LEFT)

Button(frameMenu, text="Профиль", command=OpenProfileResident).pack(side=LEFT)

OpenMainPage()

mainRoot.mainloop()
