from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self._username_field_locator = "input#user-name"
        self._password_field_locator = "input#password"
        self._login_button_locator = "input#login-button"
        self._error_message_locator = "[data-test='error']"
        self._close_error_button_locator = ".error-button"

    def enter_username(self, username) -> None:
        self.page.fill(self._username_field_locator, username)

    def enter_password(self, password) -> None:
        self.page.fill(self._password_field_locator, password)

    def click_login(self) -> None:
        self.page.click(self._login_button_locator)

    def get_error_message(self) -> Locator:
        return self.page.locator(self._error_message_locator)

    def close_error_message(self) -> None:
        self.page.click(self._close_error_button_locator)
