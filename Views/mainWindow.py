from tkinter import Tk, Frame, Button, LEFT
from Views.profileResident import GetProfileFrame
from Views.ListResidentObject import GetResidentObject
from Views.availableObject import GetAvailableObject

def ClearRoot():
    if mainRoot.winfo_children():
        mainRoot.winfo_children()[1].destroy()

def OpenProfileResident():
    global frameContent
    ClearRoot()
    frameContent = GetProfileFrame()
    frameContent.grid(row=1, column=0)

def OpenMainPage():
    global frameContent
    ClearRoot()
    frameContent = GetResidentObject()
    frameContent.grid(row=1, column=0)
    mainRoot.update()

def OpenAvailableObject():
    global frameContent
    ClearRoot()
    frameContent = GetAvailableObject()
    frameContent.grid(row=1, column=0)
    mainRoot.update()


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
