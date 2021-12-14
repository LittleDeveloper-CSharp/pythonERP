from tkinter import Frame, Button, LEFT
from Content.Profile import Profile
from Content.Object import FreeObject

class Menu(Frame):
    def __init__(self, root, frame_root, id):
        self.resident_id = id
        self.parent = root

        Frame.__init__(self, frame_root)

        Button(root, text="Главная", command=self.open_main_page).pack(side=LEFT)

        Button(root, text="Доступные помещения", command=self.open_available_object).pack(side=LEFT)

        Button(root, text="Профиль", command=self.open_profile_resident).pack(side=LEFT)

    def clear_root(self):
        if self.winfo_children():
            self.winfo_children()[1].destroy()

    def open_profile_resident(self):
        self.clear_root()
        frame_content = Profile(self.parent, self.resident_id)
        frame_content.grid(row=1, column=0)

    def open_main_page(self):
        self.clear_root()
        self.create_frame_object(get_resident_object(self.resident_id))

    def open_available_object(self):
        self.clear_root()
        frame_object = FreeObject(self.parent)
        frame_object.