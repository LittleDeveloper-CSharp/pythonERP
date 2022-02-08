from tkinter import Frame, Button, messagebox
import xlsxwriter

from Models.admin_model import get_object, get_residents, get_entity_for_report
from Views.Partial.Admin.Partial.ReportContent.ReportContentFrame import ReportContent


class ReportFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        frame_buttons = Frame(self)
        self.frame_content = Frame(self)
        Button(frame_buttons, text="Информация об арендах резидента", command=self.resident_rent).pack()
        Button(frame_buttons, text="Информация об арендах помещения", command=self.object_rent).pack()

        frame_buttons.grid(row=0, column=0)
        self.frame_content.grid(row=0, column=1)

    def __clear_frame(self):
        for item in self.frame_content.winfo_children():
            item.destroy()

    def resident_rent(self):
        self.__clear_frame()
        residents = [(i[0], i[1]) for i in get_residents()]
        ReportContent(self.frame_content, residents, self.__create_resident_rent).grid(row=0, column=1)

    def object_rent(self):
        self.__clear_frame()
        object_rent = [(i[0], i[1]) for i in get_object()]
        ReportContent(self.frame_content, object_rent, self.__create_object_rent).grid(row=0, column=1)

    def __create_resident_rent(self, date_start, date_end, resident):
        file_name = str(resident[1])
        resident[1] = "idResident"
        content = get_entity_for_report(date_start, date_end, resident)
        self.__create_excel(file_name, content)

    def __create_object_rent(self, date_start, date_end, object_rent):
        file_name = str(object_rent[1])
        object_rent[1] = "idObject"
        content = get_entity_for_report(date_start, date_end, object_rent)
        self.__create_excel(file_name, content)

    def __create_excel(self, file_name, content):
        if content == () or content == []:
            messagebox.showinfo("Ошибка", "Информация отсутствует")
            return

        workbook = xlsxwriter.Workbook(f'../{file_name}.xlsx')
        worksheet = workbook.add_worksheet()
        row = 1
        column = 0

        worksheet.write(0, 0, "Ид")
        worksheet.write(0, 1, "Резидент")
        worksheet.write(0, 2, "Объект")
        worksheet.write(0, 3, "Дата начала аренды")
        worksheet.write(0, 4, "Дата окончания аренды")
        worksheet.write(0, 5, "Стоимость аренды")
        worksheet.write(0, 6, "Статус аренды")
        worksheet.write(0, 7, "Цель аренды")

        total_sum = 0

        for item in content:
            for property_item in item:
                if column == 5:
                    total_sum += property_item
                worksheet.write(row, column, property_item)
                column += 1
            row += 1
            column = 0

        worksheet.write(len(content) + 1, 5, "Итого:")
        worksheet.write(len(content) + 1, 6, f"{total_sum} руб.")

        workbook.close()
