from playwright.async_api import Page, expect

from configs.urls import Urls
from pages.checkout_pages.base_checkout_page import BaseCheckoutPage


class YourInformationPage(BaseCheckoutPage):
    PAGE_URL: str = Urls.YOUR_INFORMATION_PAGE

    def __init__(self, page: Page):
        super().__init__(page)

        self._first_name_input = page.locator("#first-name")
        self._last_name_input = page.locator("#last-name")
        self._zip_code_input = page.locator("#postal-code")
        self._continue_button = page.locator("#continue")

    async def enter_first_name(self, first_name: str) -> None:
        await self._first_name_input.fill(first_name)
        await expect(self._first_name_input).to_have_value(first_name)

    async def enter_last_name(self, last_name: str) -> None:
        await self._last_name_input.fill(last_name)
        await expect(self._last_name_input).to_have_value(last_name)

    async def enter_zip_code(self, zip_code: str) -> None:
        await self._zip_code_input.fill(zip_code)
        await expect(self._zip_code_input).to_have_value(zip_code)

    async def click_continue(self) -> None:
        await self._continue_button.click()

    async def fill_form(self, first_name: str, last_name: str, zip_code: str) -> None:
        await self.enter_first_name(first_name)
        await self.enter_last_name(last_name)
        await self.enter_zip_code(zip_code)
