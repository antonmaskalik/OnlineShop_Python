class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


STANDARD_USER = User("standard_user", "secret_sauce")
LOCKED_OUT_USER = User("locked_out_user", "secret_sauce")
INVALID_USER = User("invalid_user", "secret_sauce")
EMPTY_USER = User("", "")
