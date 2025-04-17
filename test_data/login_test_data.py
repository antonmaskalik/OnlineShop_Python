from test_data.users import *

login_negative_cases = [
    (
        INVALID_USER,
        "Epic sadface: Username and password do not match any user in this service",
    ),
    (User(STANDARD_USER.username, ""), "Epic sadface: Password is required"),
    (User("", STANDARD_USER.password), "Epic sadface: Username is required"),
    (EMPTY_USER, "Epic sadface: Username is required"),
    (LOCKED_OUT_USER, "Epic sadface: Sorry, this user has been locked out."),
]
