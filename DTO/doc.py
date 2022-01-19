class Doc:
    def __init__(self, doc_tuple):
        self.id = doc_tuple[0]
        self.name = doc_tuple[1]
        self.description = doc_tuple[2]
        self.user_login = doc_tuple[3]
        self.path = doc_tuple[4]
