class User:
    def __init__(self, user_tuple):
        self.resident = None
        self.login = user_tuple[0]
        self.idRole = user_tuple[1]

    def set_resident(self, resident):
        self.resident = resident
