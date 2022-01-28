class Resident:
    def __init__(self, resident_info_tuple):
        self.Id = resident_info_tuple[0]
        self.login = resident_info_tuple[1]
        self.last_name = resident_info_tuple[2]
        self.first_name = resident_info_tuple[3]
        self.patronymic = resident_info_tuple[4]
        self.inn = resident_info_tuple[5]
        self.phone = resident_info_tuple[6]
        self.email = resident_info_tuple[7]
        self.photo_path = resident_info_tuple[8]
