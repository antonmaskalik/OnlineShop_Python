from abc import ABC

from playwright.async_api import Page

from pages.base_page import BasePage


class BaseCheckoutPage(BasePage, ABC):
    def __init__(self, page: Page):
        super().__init__(page)

        self._cancel_button = page.locator("button[class^='btn btn_secondary']")

    async def click_cancel(self) -> None:
        await self._cancel_button.click()
