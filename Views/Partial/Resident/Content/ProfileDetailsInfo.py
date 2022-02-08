from tkinter import Frame, Label, Entry, Button, LEFT, RIGHT, messagebox

from Models.resident_object import get_details_info
from Models.resident_object import create_details_info


class ProfileDetailsInfo(Frame):
    def __init__(self, master, resident_id, is_resident):
        super().__init__(master)

        frame_details_info = Frame(self)

        self.resident_details = get_details_info(resident_id)
        self.resident_id = resident_id

        if not is_resident:
            if self.resident_details is None or self.resident_details == ():
                Label(self, text="Информация отсутствует").pack()
                return

        Label(frame_details_info, text="БИК").pack()
        self.bik_entry = Entry(frame_details_info)
        self.bik_entry.pack()
        Label(frame_details_info, text="Банк акк").pack()
        self.bank_entry = Entry(frame_details_info)
        self.bank_entry.pack()
        Label(frame_details_info, text="КПП").pack()
        self.kpp_entry = Entry(frame_details_info)
        self.kpp_entry.pack()
        Label(frame_details_info, text="ЮР Адрес").pack()
        self.address_entry = Entry(frame_details_info)
        self.address_entry.pack()
        Label(frame_details_info, text="Реквизиты").pack()
        self.pay_acc_entry = Entry(frame_details_info)
        self.pay_acc_entry.pack()
        Label(frame_details_info, text="Индекс").pack()
        self.index_entry = Entry(frame_details_info)
        self.index_entry.pack()
        Label(frame_details_info, text="Кор акк").pack()
        self.cor_acc_entry = Entry(frame_details_info)
        self.cor_acc_entry.pack()
        Label(frame_details_info, text="ИП название").pack()
        self.name_entry = Entry(frame_details_info)
        self.name_entry.pack()
        Label(frame_details_info, text="День рождения").pack()
        self.birthday_entry = Entry(frame_details_info)
        self.birthday_entry.pack()
        Label(frame_details_info, text="Паспорт (серия, номер)").pack()
        frame_passport = Frame(frame_details_info)
        self.passport_seria = Entry(frame_passport)
        self.passport_seria.pack(side=LEFT)
        self.passport_number = Entry(frame_passport)
        self.passport_number.pack(side=RIGHT)
        frame_passport.pack()
        Label(frame_details_info, text="Паспорт выдан кем?").pack()
        self.passport_issued = Entry(frame_details_info)
        self.passport_issued.pack()
        Label(frame_details_info, text="Когда выдан?").pack()
        self.passport_date_issued = Entry(frame_details_info)
        self.passport_date_issued.pack()

        Label(frame_details_info, text="Номер сертификата").pack()
        self.certificate_entry = Entry(frame_details_info)
        self.certificate_entry.pack()

        Button(frame_details_info, command=self.__save_change, text="Принять изменения").pack()

        frame_details_info.pack()

        if self.resident_details is not None and self.resident_details != ():
            self.__fill_entry()

    @staticmethod
    def __error_message(message_title, message_description):
        messagebox.showerror(message_title, message_description)

    def validate_numeric(self, name, value):
        if value == '' or not value.isnumeric():
            self.__error_message("Ошибка", f'Некорректное значение - {name} (Нужны только цифры)')
            return False
        return True

    def validate_text(self, name, value):
        if value == '' or value.isspace():
            self.__error_message("Ошибка", f'Некорректное значение - {name} (Нужно текст)')
            return False
        return True

    def __save_change(self):
        if not self.validate_numeric("Серия паcпорта", self.passport_seria.get()):
            return

        if not self.validate_numeric("Номер паспорта", self.passport_number.get()):
            return

        if not self.validate_numeric("Номер бик", self.bik_entry.get()):
            return

        if not self.validate_numeric("Банковский счет", self.bank_entry.get()):
            return

        if not self.validate_numeric("Номер КПП", self.kpp_entry.get()):
            return

        if not self.validate_text("Адрес", self.address_entry.get()):
            return

        if not self.validate_numeric("Реквизиты", self.pay_acc_entry.get()):
            return

        if not self.validate_numeric("Индекс", self.index_entry.get()):
            return

        if not self.validate_numeric("Кор аккаунт",  self.cor_acc_entry.get()):
            return

        if not self.validate_text("Наименование организации", self.name_entry.get()):
            return

        if not self.validate_text("День рождения", self.birthday_entry.get()):
            return

        if not self.validate_text("Отдел выдачи паспорта", self.passport_issued.get()):
            return

        if not self.validate_text("Дата выдачи паспорта", self.passport_date_issued.get()):
            return

        if not self.validate_numeric("Номер сертификата", self.certificate_entry.get()):
            return

        passport = f'{self.passport_seria.get()} {self.passport_number.get()}'
        create_details_info((self.resident_id, self.bik_entry.get(), self.bank_entry.get(), self.kpp_entry.get(),
                             self.address_entry.get(), self.pay_acc_entry.get(), self.index_entry.get(),
                             self.cor_acc_entry.get(), self.name_entry.get(), self.birthday_entry.get(), passport,
                             self.passport_issued.get(), self.passport_date_issued.get(), self.certificate_entry.get()))

        self.master.destroy()

    def __fill_entry(self):
        self.bik_entry.insert(0, self.resident_details[2])
        self.bank_entry.insert(0, self.resident_details[3])
        self.kpp_entry.insert(0, self.resident_details[4])
        self.address_entry.insert(0, self.resident_details[5])
        self.pay_acc_entry.insert(0, self.resident_details[6])
        self.index_entry.insert(0, self.resident_details[7])
        self.cor_acc_entry.insert(0, self.resident_details[8])
        self.name_entry.insert(0, self.resident_details[9])
        self.birthday_entry.insert(0, self.resident_details[10])

        passport_seria, passport_number = self.resident_details[11].split(' ')

        self.passport_seria.insert(0, passport_seria)
        self.passport_number.insert(0, passport_number)
        self.passport_issued.insert(0, self.resident_details[12])
        self.passport_date_issued.insert(0, self.resident_details[13])

        self.certificate_entry.insert(0, self.resident_details[14])
