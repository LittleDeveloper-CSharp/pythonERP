from Models.resident_object import cancellation_rent
from Views.Pagination.PaginationItem.common_pagination_item import PaginationItem
from tkinter import Toplevel, messagebox

from Views.object_detail_info import DetailsInfo


def _open_window(select_object, resident, delegate_refresh):
    details_info = Toplevel()
    details_info.title("Подробная информация")
    DetailsInfo(parent=details_info, object_dto=select_object, resident=resident,
                refresh_frame=delegate_refresh).pack()


def _cancellation_rent(resident, select_object, delegate_refresh):
    if messagebox.askokcancel("Подтверждение", "Вы уверены?"):
        cancellation_rent(resident.Id, select_object.Id)
        delegate_refresh()


class ResidentObjectPartial(PaginationItem):
    def __init__(self, resident_object, resident, delegate_refresh=None):
        event = ("Подробнее", lambda: _open_window(resident_object, resident, delegate_refresh))
        config = None
        if resident_object.idStatus == 2:
            config = {'frame': {'background': "gray"}, 'label': {
                'text': str(resident_object.Name) + " - Не подтвержден",
                      'bg': 'gray',
                      'fg': 'white'}}
            event = ("Отменить ожидание", lambda: _cancellation_rent(resident_object, resident, delegate_refresh))
        super().__init__(resident_object, event, config)
