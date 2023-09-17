import datetime


class Entry:
    i_d = 0
    title = ''
    body = ''
    date = datetime.datetime.now()

    def set_id(self, i_d: int):
        self.i_d = i_d

    def get_id(self):
        return self.i_d

    def set_title(self, title: str):
        self.title = title

    def get_title(self):
        return self.title

    def set_body(self, body: str):
        self.body = body

    def get_body(self):
        return self.body

    def set_date(self, date: datetime):
        self.date = date

    def get_date(self):
        return self.date


