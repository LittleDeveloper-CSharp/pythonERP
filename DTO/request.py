class Request:
    def __init__(self, item):
        self.Id = item[0]
        self.Name = item[1]
        self.Status = None


class RequestForRent(Request):
    def __init__(self, item):
        super().__init__(item)
        self.Status = "Ожидает подтверждения аренды"


class RequestForUpdate(Request):
    def __init__(self, item):
        super().__init__(item)
        self.Status = "Ожидает изменения"
