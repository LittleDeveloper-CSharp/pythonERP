from tkinter import Frame, Button, LEFT
from Views.Partial.Resident.Content.ProfileWidget import Profile
from Views.Partial.Resident.Content.FreeObjectWidget import FreeObject
from Views.Partial.Resident.Content.RentObjectWidget import RentObjectWidget


class ResidentMenu(Frame):
    def __init__(self, frame_menu, resident_id):
        self.resident_id = resident_id
        self.content = Frame()

        Frame.__init__(self, frame_menu)

        Button(frame_menu, text="Главная", command=self.resident_objects).pack(side=LEFT)

        Button(frame_menu, text="Доступные помещения", command=self.free_object).pack(side=LEFT)

        Button(frame_menu, text="Профиль", command=self.profile_resident).pack(side=LEFT)

        self.resident_objects()

    def destroy_widget(self):
        if self.content is not None:
            self.content.grid_forget()

    def profile_resident(self):
        self.destroy_widget()
        self.content = Profile(self.resident_id)
        self.content.grid(row=1, column=0)

    def free_object(self):
        self.destroy_widget()
        self.content = FreeObject(self.resident_id)
        self.content.grid(row=1, column=0)

    def resident_objects(self):
        self.destroy_widget()
        self.content = RentObjectWidget(self.resident_id)
        self.content.grid(row=1, column=0)

