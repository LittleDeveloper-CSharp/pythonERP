from tkinter import Frame, Button, Label, LEFT, Entry, VERTICAL, Scrollbar
from tkinter.ttk import Treeview


class ReportContent(Frame):
    def __init__(self, master, list_item, function_create):
        super().__init__(master)

        self.create_excel = function_create

        self.table_item = Treeview(self, show="headings", columns=("#1", "#2"))
        self.table_item.heading("#1", text="id")
        self.table_item.heading("#2", text="Наименование")
        ysb = Scrollbar(self, orient=VERTICAL, command=self.table_item.yview)
        self.table_item.config(yscrollcommand=ysb.set)

        self.table_item.pack()

        self.table_item.bind("<<TreeviewSelect>>", self.selected_item)

        frame_date = Frame(self)

        Label(frame_date, text="С").pack(side=LEFT)
        self.date_start = Entry(frame_date)
        self.date_start.pack(side=LEFT)
        Label(frame_date, text="По").pack(side=LEFT)
        self.date_end = Entry(frame_date)
        self.date_end.pack(side=LEFT)

        self.select_item = None

        frame_date.pack()

        Button(self, command=self.create_report, text="Сформировать").pack()

        if list_item != ():
            self.fill_treeview(list_item)

    def fill_treeview(self, list_item):
        for item in list_item:
            self.table_item.insert("", "end", values=(item[0], item[1]))

    def create_report(self):
        if self.select_item is not None:
            self.create_excel(self.date_start.get(), self.date_end.get(), self.select_item)

    def selected_item(self, event):
        select_item = self.table_item.selection()

        if select_item is not None:
            self.select_item = self.table_item.item(select_item[0])["values"]
