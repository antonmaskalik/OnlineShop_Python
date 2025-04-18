from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self._username_field = page.locator("input#user-name")
        self._password_field = page.locator("input#password")
        self._login_button = page.locator("input#login-button")
        self._error_message = page.locator("[data-test='error']")
        self._close_error_button = page.locator(".error-button")

    def enter_username(self, username) -> None:
        self._username_field.fill(username)
        expect(self._username_field).to_have_value(username)

    def enter_password(self, password) -> None:
        self._password_field.fill(password)
        expect(self._password_field).to_have_value(password)

    def click_login(self) -> None:
        self._login_button.click()

    def close_error_message(self) -> None:
        self._close_error_button.click()

    def chck_error_message(self, expected_message) -> None:
        expect(self._error_message).to_be_visible()
        expect(self._error_message).to_have_text(expected_message)
