from Service.Helper.PaginataionItem import PaginationItem


class ResidentObjectPartial(PaginationItem):
    def __init__(self, resident_object):
        super().__init__(resident_object)
