from Service.opener_photo import set_photo


class RequestRentObject:
    def __init__(self, request_tuple):
        self.id = request_tuple[0]
        self.resident_id = request_tuple[1]
        self.object_id = request_tuple[2]
        self.date_start = request_tuple[3]
        self.date_end = request_tuple[4]
        self.total_sum = request_tuple[5]
        self.status_id = request_tuple[6]
        self.area = request_tuple[7]
        self.photo = set_photo(request_tuple[8])
