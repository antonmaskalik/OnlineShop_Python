class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


STANDARD_USER: User = User("standard_user", "secret_sauce")
LOCKED_OUT_USER: User = User("locked_out_user", "secret_sauce")
INVALID_USER: User = User("invalid_user", "secret_sauce")
EMPTY_USER: User = User("", "")
