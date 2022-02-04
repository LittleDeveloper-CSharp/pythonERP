from tkinter import Toplevel, messagebox

from Views.Pagination.PaginationItem.common_pagination_item import PaginationItem
from Views.object_detail_info import DetailsInfo


def _open_window(select_object, resident, delegate_refresh):
    details_info = Toplevel()
    details_info.title("Подробная информация")
    DetailsInfo(parent=details_info, object_dto=select_object, resident=resident,
                refresh_frame=delegate_refresh).pack()


class ObjectPartial(PaginationItem):
    def __init__(self, available_object, resident=None, delegate_refresh=None):
        event = ("Подробнее", lambda: messagebox.showinfo("Ошибка", "Тут пока ничего нет"))
        if resident is not None:
            event = ("Подробнее", lambda: _open_window(available_object, resident, delegate_refresh))
        super().__init__(available_object, event)
