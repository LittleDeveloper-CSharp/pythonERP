from tkinter import Frame, Label


class RequestForUpdateFrame(Frame):
    def __init__(self, master, request):
        super().__init__(master)
        _PartialRequest(self, request[0]).grid(row=0, column=0)
        Label(self, text="->").grid(row=0, column=1)
        _PartialRequest(self, request[1]).grid(row=0, column=2)


class _PartialRequest(Frame):
    def __init__(self, master, request):
        super().__init__(master)
        Label(self, text=f"Логин: {request[1]}").pack()
        Label(self, text=f"Фамилия: {request[2]}").pack()
        Label(self, text=f"Имя: {request[3]}").pack()
        Label(self, text=f"Отчество: {request[4]}").pack()
        Label(self, text=f"ИНН: {request[5]}").pack()
        Label(self, text=f"Телефон: {request[6]}").pack()
        Label(self, text=f"Email: {request[7]}").pack()
