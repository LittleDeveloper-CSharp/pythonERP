import os
from pathlib import Path
from tkinter import Frame, Listbox, Button, LEFT, RIGHT, Entry, Label, END, filedialog, messagebox
from shutil import copyfile

from DTO.doc import Doc
from Models.resident_object import docs_by_user, create_doc_for_user, doc_by_id, update_doc, delete_doc


def change_state_container(container, state):
    for child in container.winfo_children():
        if len(child.children) > 1:
            for inner_child in child.winfo_children():
                inner_child.configure(state=state)
        else:
            child.configure(state=state)


class DocsFrame(Frame):
    def __init__(self, master, resident_login):
        super().__init__(master)
        self.file_path = None
        self.is_create_doc = False
        self.select_doc = None

        self.frame_list_doc = Frame(self)

        self.resident_login = resident_login
        self.list_docs = Listbox(self.frame_list_doc)
        self.list_docs.pack()
        self.list_docs.bind("<<ListboxSelect>>", self.__selecting_doc)

        frame_button = Frame(self.frame_list_doc)
        Button(frame_button, text="Удалить", command=self.__delete_doc).pack(side=LEFT)
        Button(frame_button, text="Добавить новый", command=self.__create_doc).pack(side=RIGHT)
        self.frame_list_doc.grid(row=0, column=0)

        frame_button.pack()

        self.frame_info_doc = Frame(self)

        frame_name_doc = Frame(self.frame_info_doc)
        Label(frame_name_doc, text="Название").pack()
        self.entry_name = Entry(frame_name_doc)
        self.entry_name.pack()
        frame_name_doc.pack()

        frame_description = Frame(self.frame_info_doc)
        Label(frame_description, text="Подробная информация").pack()
        self.entry_description = Entry(frame_description)
        self.entry_description.pack()
        frame_description.pack()

        self.frame_create_doc = Frame(self.frame_info_doc)
        Button(self.frame_create_doc, text="Отмена", command=self.__cancellation_create_doc).pack(side=LEFT)
        Button(self.frame_create_doc, text="Указать путь", command=self.__ask_file_path).pack(side=LEFT)

        frame_manipulation = Frame(self.frame_info_doc)
        Button(frame_manipulation, text="Открыть файл", command=self.__open_file).pack(side=LEFT)
        self.accept_button = Button(frame_manipulation, text="Изменить", command=self.__accept_update_doc)
        self.accept_button.pack(side=LEFT)
        frame_manipulation.pack()

        self.frame_info_doc.grid(row=0, column=1)

        self.__fill_list_box()

    def __create_doc(self):
        self.file_path = None
        self.entry_description.delete(0, END)
        self.entry_name.delete(0, END)
        change_state_container(self.frame_list_doc, 'disabled')
        self.accept_button['text'] = "Добавить"
        self.is_create_doc = True
        self.accept_button['command'] = self.__accept_create_doc
        self.frame_create_doc.pack()
        change_state_container(self.frame_info_doc, 'normal')

    def __delete_doc(self):
        if not self.is_create_doc and self.select_doc is not None:
            if messagebox.askquestion("Подтверждение", "Подтвердите удаление") == 'yes':
                delete_doc(self.select_doc.Id)
                self.__cancellation_create_doc()

    def __accept_create_doc(self):
        if self.file_path is not None or self.select_doc is not None:
            doc_tuple = (0, self.entry_name.get(), self.entry_description.get(), self.resident_login, self.file_path)
            doc = Doc(doc_tuple)

            new_doc_path = f'../Resources/docs/{self.resident_login}/{doc.name}.' \
                           f'{doc.path.split(".")[len(doc.path.split(".")) - 1]}'

            copyfile(doc.path, new_doc_path)
            doc.path = new_doc_path
            create_doc_for_user(doc)
            self.__cancellation_create_doc()

    def __accept_update_doc(self):
        self.select_doc.name = self.entry_name.get()
        self.select_doc.description = self.entry_description.get()
        update_doc(self.select_doc)
        self.__cancellation_create_doc()

    def __cancellation_create_doc(self):
        self.entry_description.delete(0, END)
        self.entry_name.delete(0, END)
        self.accept_button['text'] = "Изменить"
        self.accept_button['command'] = self.__accept_update_doc
        self.frame_create_doc.pack_forget()
        change_state_container(self.frame_list_doc, 'normal')
        self.is_create_doc = False
        self.file_path = None
        self.select_doc = None
        self.__fill_list_box()

    def __ask_file_path(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path == '':
            self.file_path = None

    def __open_file(self):
        if (self.is_create_doc and self.file_path is not None) or \
                (not self.is_create_doc and self.select_doc is not None):
            file_path = self.file_path
            if self.accept_button['text'] == "Изменить":
                file_path = Path(self.select_doc.path)
            os.startfile(file_path)
        else:
            if self.is_create_doc:
                messagebox.showerror("Ошибка", "Укажите путь к файлу")
            else:
                messagebox.showerror("Ошибка", "Выберите файл в списке")

    def __fill_list_box(self):
        self.list_docs.delete(0, END)
        self.docs = [Doc(i) for i in docs_by_user(self.resident_login)]
        for doc in self.docs:
            self.list_docs.insert(0, (doc.id, doc.name))
        change_state_container(self.frame_info_doc, 'disabled')

    def __selecting_doc(self, event):
        selection = self.list_docs.curselection()
        if selection:
            change_state_container(self.frame_info_doc, 'normal')
            self.entry_name.delete(0, END)
            self.entry_description.delete(0, END)
            index = selection[0]
            doc_id = event.widget.get(index)[0]
            self.select_doc = Doc(doc_by_id(doc_id))
            self.entry_name.insert(0, self.select_doc.name)
            self.entry_description.insert(0, self.select_doc.description)
