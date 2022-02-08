from Models.admin_model import get_resident
from Views.Pagination.PaginationItem.common_pagination_item import PaginationItem
from types import SimpleNamespace
from tkinter import Toplevel
from Views.Partial.Resident.Content.docs_frame import DocsFrame
from Views.Partial.Resident.Content.profile import Profile


def _open_window(resident_id):
    detail_info_resident = Toplevel()
    detail_info_resident.grab_set()
    Profile(detail_info_resident, resident_id, False).grid(row=0, column=0)
    resident_login = get_resident(resident_id)[1]
    DocsFrame(detail_info_resident, resident_login).grid(row=0, column=1)


class ResidentPartial(PaginationItem):
    def __init__(self, resident):
        item = SimpleNamespace(Id=resident.Id, Name=f"{resident.last_name} {resident.first_name}",
                               photo_path=resident.photo_path)
        event = ("Подробнее", lambda: _open_window(item.Id))
        super().__init__(item, event)
