from Views.Partial.Resident.Content.ListObject import ListObject
from Models.ObjectModel import GetFreeObject

class FreeObject(Frame):
    def __init__(self, root):
        Frame().__init__(self, root)
        objects = GetFreeObject()
        self.parent = ListObject(objects)
