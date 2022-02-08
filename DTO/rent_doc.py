import datetime


class RentDoc:
    day_now = None
    month_now = None
    year_now = None
    person_fullname = None
    passport_seria = None
    passport_number = None
    passport_issued = None
    passport_day = None
    passport_month = None
    passport_year = None
    person_birthday = None
    person_birth_month = None
    person_birth_year = None
    ip_name = None
    certificate_number = None
    object_square = None
    cadastral_number = None
    certificate_of_ownership = None
    purpose_of_the_lease = None
    day_date_start = None
    month_date_start = None
    year_date_start = None
    day_date_end = None
    month_date_end = None
    year_date_end = None
    sum = None
    person_email = None
    person_address = None
    person_index = None
    person_inn = None
    person_kpp = None
    person_bank = None
    person_pay_acc = None
    person_cor_acc = None
    person_bik = None

    def set_day(self, date_start, date_end):
        date_start = date_start.split('.')
        date_end = date_end.split('.')
        self.day_date_start = date_start[0]
        self.month_date_start = date_start[1]
        self.year_date_start = date_start[2]
        self.day_date_end = date_end[0]
        self.month_date_end = date_end[1]
        self.year_date_end = date_end[2]

        date_now = datetime.datetime.today()

        self.day_now = date_now.day
        self.month_now = date_now.month
        self.year_now = date_now.year

    def set_resident(self, resident_info):
        self.person_fullname = resident_info.full_name
        self.person_bik = resident_info.bik
        self.person_bank = resident_info.bank
        self.person_inn = resident_info.inn
        self.person_kpp = resident_info.kpp
        self.person_address = resident_info.address
        self.person_pay_acc = resident_info.pay_acc
        self.person_index = resident_info.index
        self.person_email = resident_info.email
        self.person_cor_acc = resident_info.cor_acc
        self.person_birthday = resident_info.birthday
        self.person_birth_month = resident_info.birthday
        self.person_birth_year = resident_info.birthday
        self.ip_name = resident_info.ip_name

        self.passport_seria = resident_info.passport_seria
        self.passport_number = resident_info.passport_number
        self.passport_issued = resident_info.passport_issued
        self.passport_day = resident_info.passport_day
        self.passport_month = resident_info.passport_month
        self.passport_year = resident_info.passport_year

        self.certificate_number = resident_info.certificate_number

    def set_object(self, object_info):
        self.cadastral_number = object_info.cadastral_number
        self.object_square = object_info.object_square
        self.purpose_of_the_lease = object_info.purpose_of_the_lease
        self.sum = object_info.sum


class ObjectForDoc:
    def __init__(self, object_info):
        self.cadastral_number = object_info[0]
        self.object_square = object_info[1]
        self.purpose_of_the_lease = object_info[2]
        self.sum = object_info[3]


class ResidentForDoc:
    def __init__(self, resident_info):
        self.full_name = f'{resident_info[0]} {resident_info[1]} {resident_info[2]}'
        self.bik = resident_info[3]
        self.bank = resident_info[4]
        self.inn = resident_info[5]
        self.kpp = resident_info[6]
        self.address = resident_info[7]
        self.pay_acc = resident_info[8]
        self.index = resident_info[9]
        self.email = resident_info[10]
        self.cor_acc = resident_info[11]
        birthday = resident_info[12].split('.')
        self.birthday = birthday[0]
        self.birth_month = birthday[1]
        self.birth_year = birthday[2]
        self.ip_name = resident_info[13]

        passport_seria, passport_number = resident_info[14].split(' ')

        self.passport_seria = passport_seria
        self.passport_number = passport_number
        self.passport_issued = resident_info[15]
        passport_date_issued = resident_info[16].split('.')
        self.passport_day = passport_date_issued[0]
        self.passport_month = passport_date_issued[1]
        self.passport_year = passport_date_issued[2]

        self.certificate_number = resident_info[17]
