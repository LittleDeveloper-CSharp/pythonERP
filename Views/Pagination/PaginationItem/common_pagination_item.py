from Service.opener_photo import set_photo


class PaginationItem:
    def __init__(self, item, event=None, config=None):
        self.Id = item.Id
        self.Name = item.Name
        self.Photo = set_photo(item.photo_path)
        if event is not None:
            self.event = event
        if config is not None:
            self.config = config
