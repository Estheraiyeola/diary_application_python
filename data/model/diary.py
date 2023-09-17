class Diary:
    i_d = 0
    username = ''
    password = ''
    entries = []

    def set_id(self, i_d: int) -> None:
        self.i_d = i_d

    def get_id(self) -> int:
        return self.i_d

    def set_username(self, username: str) -> None:
        self.username = username

    def get_username(self) -> str:
        return self.username

    def set_password(self, password: str) -> None:
        self.password = password

    def get_password(self) -> str:
        return self.password


