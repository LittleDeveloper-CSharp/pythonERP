from Views.Partial.Resident.Content.ListObject import ListObject
from Models.ResidentObject import GetRentObject
from tkinter import Frame

class RentObject(Frame):
    def __init__(self, root, id):
        Frame().__init__(self, root)
        object = GetRentObject(id)
        self.parent  = ListObject(object)
