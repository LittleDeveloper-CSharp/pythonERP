from tkinter import Frame, Label, Button, Entry, LEFT, RIGHT
from tkinter.filedialog import askopenfilename

from DTO.object_market_place import ObjectModel
from Models.admin_model import update_object, delete_object, create_object
from Service.copy_file import copy_file
from Service.opener_photo import set_photo


class ObjectDetailsAdmin(Frame):
    def __init__(self, master, object_info, delegate_refresh):
        super().__init__(master)
        self.new_photo_path = None
        self.delegate_refresh = delegate_refresh

        frame_photo = Frame(self)

        image = None

        frame_photo.grid(row=0, column=0)
        self.object_info = object_info

        if object_info.Id is None:
            self.object_info = ObjectModel()
            self.object_info.Id = 0
        else:
            image = set_photo(object_info.photo_path)

        self.photo_place = Label(frame_photo, image=image)
        self.photo_place.image = image
        self.photo_place.pack()

        Button(frame_photo, command=self.__change_photo, text="Изменить фото").pack()
        frame_details_info = Frame(self)
        Label(frame_details_info, text="Наименование").pack()
        self.entry_name = Entry(frame_details_info)
        self.entry_name.pack()
        Label(frame_details_info, text="Стоимость аренды").pack()
        self.entry_rent_price = Entry(frame_details_info)
        self.entry_rent_price.pack()
        Label(frame_details_info, text="Площадь").pack()
        self.entry_area = Entry(frame_details_info)
        self.entry_area.pack()
        Label(frame_details_info, text="Статус").pack()
        self.label_status = Label(frame_details_info)
        self.label_status.pack()

        button_frame = Frame(frame_details_info)
        Button(frame_details_info, text="Обновить", command=self.__accept_update).pack(side=LEFT)
        Button(frame_details_info, text="Удалить", command=self.__delete_object).pack(side=RIGHT)

        button_frame.pack()

        if self.object_info.Id != 0:
            self.__fill_entry()

        frame_details_info.grid(row=0, column=1)

    def __fill_entry(self):
        self.entry_name.insert(0, self.object_info.Name)
        self.entry_rent_price.insert(0, self.object_info.rentPrice)
        self.entry_area.insert(0, self.object_info.Area)
        self.label_status['text'] = self.object_info.idStatus

    def __change_photo(self):
        file_path = askopenfilename()

        if file_path is None:
            return

        image = set_photo(file_path)
        self.photo_place.config(image=image)
        self.photo_place.image = image
        self.new_photo_path = file_path

    def __accept_update(self):
        self.object_info.Name = self.entry_name.get()
        self.object_info.Area = self.entry_area.get()
        self.object_info.rentPrice = self.entry_rent_price.get()
        if self.new_photo_path is not None:
            path_file_tuple = self.new_photo_path.split('.')

            new_file_path = '../Resources/image/' + self.object_info.Name + '.' \
                            + path_file_tuple[len(path_file_tuple) - 1]

            copy_file(self.new_photo_path, new_file_path)

            self.object_info.photo_path = new_file_path

        if self.object_info.Id != 0:
            update_object(self.object_info)
        else:
            create_object(self.object_info)

        self.delegate_refresh()
        self.master.destroy()

    def __delete_object(self):
        delete_object(self.object_info.Id)
        self.delegate_refresh()
        self.master.destroy()
