from playwright.async_api import Page, expect

from pages.base_page import BasePage
from test_data.users import User


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self._username_field = page.locator("input#user-name")
        self._password_field = page.locator("input#password")
        self._login_button = page.locator("input#login-button")
        self._error_message = page.locator("[data-test='error']")
        self._close_error_button = page.locator(".error-button")

    async def enter_username(self, username: str) -> None:
        await self._username_field.fill(username)
        await expect(self._username_field).to_have_value(username)

    async def enter_password(self, password: str) -> None:
        await self._password_field.fill(password)
        await expect(self._password_field).to_have_value(password)

    async def click_login(self) -> None:
        await self._login_button.click()

    async def close_error_message(self) -> None:
        await self._close_error_button.click()

    async def login(self, user: User) -> None:
        await self.enter_username(user.username)
        await self.enter_password(user.password)
        await self.click_login()

    async def chck_error_message(self, expected_message) -> None:
        await expect(self._error_message).to_have_text(expected_message)
