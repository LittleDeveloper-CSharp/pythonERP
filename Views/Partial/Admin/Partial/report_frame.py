import datetime
from tkinter import Frame, Button, messagebox, Entry, Label
import xlsxwriter

from Models.admin_model import get_object, get_residents, get_entity_for_report, get_object_for_report, \
    get_rent_for_report
from Views.Partial.Admin.Partial.ReportContent.ReportContentFrame import ReportContent


class ReportFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        frame_buttons = Frame(self)
        self.frame_content = Frame(self)
        Button(frame_buttons, text="Информация об арендах резидента", command=self.__resident_rent_click).pack()
        Button(frame_buttons, text="Информация о выручке с помещения", command=self.__object_rent_click).pack()
        Button(frame_buttons, text="Информация о занятых помемщениях", command=self.__create_occupied_premises_click).pack()
        Button(frame_buttons, text="Информация о свободных помещениях", command=self.__create_free_premises_click).pack()
        Button(frame_buttons, text="Итоговая выручка", command=self.__total_sum_click).pack()

        frame_buttons.grid(row=0, column=0)
        self.frame_content.grid(row=0, column=1)

    def __clear_frame(self):
        for item in self.frame_content.winfo_children():
            item.destroy()

    def __resident_rent_click(self):
        self.__clear_frame()
        residents = [(i[0], i[1]) for i in get_residents()]
        ReportContent(self.frame_content, residents, self.__create_resident_rent).grid(row=0, column=1)

    def __object_rent_click(self):
        self.__clear_frame()
        object_rent = [(i[0], i[1]) for i in get_object()]
        ReportContent(self.frame_content, object_rent, self.__create_object_rent).grid(row=0, column=1)

    def __create_occupied_premises_click(self):
        self.__clear_frame()
        self.__create_occupied_premises()

    def __create_free_premises_click(self):
        self.__clear_frame()
        self.__create_free_premises()

    def __total_sum_click(self):
        self.__clear_frame()
        self.__single_frame(self.__create_total_sum)

    def __create_occupied_premises(self):
        occupied_premises = get_object_for_report((1, 2))
        header = ("Наименование объекта", "Стоимость аренды", "Площадь", "Статус", "Кадастровый номер")
        footer = {'Итого занятых помещений: ': len(occupied_premises)}
        self.__create_excel(f"Занятые помещения", header, occupied_premises, footer)

    def __create_free_premises(self):
        free_premises = get_object_for_report((4, 4))
        header = ("Наименование объекта", "Стоимость аренды", "Площадь", "Статус", "Кадастровый номер")
        footer = {'Итого свободных помещений': len(free_premises)}
        self.__create_excel(f"Свободные помещения", header, free_premises, footer)

    def __create_total_sum(self, date_start, date_end):
        total_sum = get_rent_for_report(date_start, date_end)
        header = ("ФИО резидента", "Наименование объекта", "Дата старта аренды", "Дата окончания аренды",
                  "Сумма аренды", "Статус", "Цель аренды")
        footer = {"Итого: ": sum([int(i[4]) for i in total_sum])}
        self.__create_excel(f"Итоговая прибыль {date_start} - {date_end}", header, total_sum, footer)

    def __single_frame(self, create_function):
        content = Frame(self.frame_content)

        date_start_entry = Entry(content)
        date_end_entry = Entry(content)
        Label(content, text="Отсчет с").pack()
        date_start_entry.pack()
        Label(content, text="По").pack()
        date_end_entry.pack()

        Button(content, text="Подтвердить", command=lambda: create_function(date_start_entry.get(),
                                                                            date_end_entry.get())).pack()

        content.grid(row=0, column=1)

    def __create_resident_rent(self, date_start, date_end, resident):
        file_name = str(resident[1])
        resident[1] = "idResident"
        header = ("ИД", "ФИО резидента", "Наименование помещения", "Дата начала аренды", "Дата окончания аренды", "Сумма аренды", "Статус",
                  "Цель аренды")
        content = get_entity_for_report(date_start, date_end, resident)
        footer = {'Итого': sum([int(i[5]) for i in content])}
        self.__create_excel(file_name, header, content, footer)

    def __create_object_rent(self, date_start, date_end, object_rent):
        file_name = str(object_rent[1])
        object_rent[1] = "idObject"
        header = ("ИД", "ФИО резидента", "Наименование объекта", "Дата начала аренды", "Дата окончания аренды", "Сумма аренды", "Статус",
                  "Цель аренды")
        content = get_entity_for_report(date_start, date_end, object_rent)
        footer = {'Итого': sum([int(i[5]) for i in content])}
        self.__create_excel(file_name, header, content, footer)

    @staticmethod
    def __create_excel(file_name, header, content, footer=None):
        if content == () or content == []:
            messagebox.showinfo("Ошибка", "Информация отсутствует")
            return

        workbook = xlsxwriter.Workbook(f'../{file_name}.xlsx')
        worksheet = workbook.add_worksheet()
        row = 0
        column = 0

        worksheet.write(0, 0, file_name)

        worksheet.write(0, len(header) - 2, "Дата создания")

        worksheet.write(0, len(header) - 1, datetime.datetime.utcnow(),
                        workbook.add_format({'num_format': 'dd/mm/yy hh:mm'}))

        row += 1

        for title in header:
            worksheet.write(row, column, title)
            column += 1

        column = 0
        row += 1

        for item in content:
            for property_item in item:
                worksheet.write(row, column, property_item)
                column += 1
            row += 1
            column = 0

        row += 1

        if footer is not None:
            for key in footer:
                worksheet.write(row, 0, key)
                worksheet.write(row, 1, footer[key])

        workbook.close()
