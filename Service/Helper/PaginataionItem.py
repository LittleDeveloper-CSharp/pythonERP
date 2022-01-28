from Service.Helper.OpenerPhoto import set_photo


class PaginationItem:
    def __init__(self, item):
        self.Id = item.Id
        self.Name = item.Name
        self.Photo = set_photo(item.photo_path)
