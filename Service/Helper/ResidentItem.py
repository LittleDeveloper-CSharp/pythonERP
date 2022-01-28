from Service.Helper.PaginataionItem import PaginationItem
from types import SimpleNamespace


class ResidentPartial(PaginationItem):
    def __init__(self, resident):
        item = SimpleNamespace(Id=resident.Id, Name=f"{resident.last_name} {resident.first_name}",
                               photo_path=resident.photo_path)
        super().__init__(item)
