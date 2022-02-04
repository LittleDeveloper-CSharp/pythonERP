import math
from tkinter import Frame, Label, Button, LEFT, RIGHT


class PaginationList(Frame):
    def __init__(self, master, list_items):
        super().__init__(master)
        if len(list_items) == 0:
            Label(self, text="Информация отсутствует").pack()
            return

        self.max_count_column = 5
        self.max_items_on_list = 5

        self.list_items = list_items
        self.index_list = 0
        self.count_list = math.ceil(len(self.list_items) / self.max_items_on_list)

        self.fill_frame()

    def clear_frame(self):
        for i in self.winfo_children():
            i.destroy()

    def fill_frame(self):
        self.clear_frame()
        index = 0
        main_content_frame = Frame(self)

        items = self.list_items[self.index_list*self.max_items_on_list:
                                self.max_items_on_list+self.index_list*self.max_items_on_list]

        for i in range(math.ceil(len(items) / self.max_count_column)):
            for j in range(self.max_count_column):
                if index == len(items):
                    break

                item = items[index]

                item_place = Frame(main_content_frame)
                photo_place = Label(item_place, image=item.Photo)
                text = Label(item_place, text=item.Name)

                if hasattr(item, "config"):
                    if "frame" in item.config:
                        item_place.config(item.config.get("frame"))
                    if "photo" in item.config:
                        photo_place.config(item.config.get("photo"))
                    if "label" in item.config:
                        text.config(item.config.get("label"))

                photo_place.pack(padx=10, pady=(10, 0))
                text.pack(padx=10, pady=(10, 0))

                if hasattr(item, "event"):
                    Button(item_place, text=item.event[0], command=item.event[1]).pack()

                item_place.grid(row=i, column=j, padx=10, pady=10)
                index += 1

        main_content_frame.grid(row=1, column=0)
        self.__create_panel_control()

    def __create_panel_control(self):
        if self.count_list == 1 and len(self.list_items) <= self.max_count_column:
            return

        frame_size_panel = Frame(self)
        Button(frame_size_panel, text="5", command=lambda: self.change_size(5)).pack(side=LEFT)
        Button(frame_size_panel, text="10", command=lambda: self.change_size(10)).pack(side=LEFT)
        Button(frame_size_panel, text="15", command=lambda: self.change_size(15)).pack(side=LEFT)
        frame_size_panel.grid(row=0, column=0)

        frame_pagination = Frame(self)
        Button(frame_pagination, text="<<", command=self.__back_list).pack(side=LEFT)
        Button(frame_pagination, text=">>", command=self.__next_list).pack(side=RIGHT)
        frame_pagination.grid(row=2, column=0)

    def change_size(self, size):
        self.max_items_on_list = size
        self.index_list = 0
        self.count_list = math.ceil(len(self.list_items) / self.max_items_on_list)
        self.fill_frame()

    def __back_list(self):
        if self.index_list != 0:
            self.index_list -= 1
            self.fill_frame()

    def __next_list(self):
        if self.index_list + 1 < self.count_list:
            self.index_list += 1
            self.fill_frame()
