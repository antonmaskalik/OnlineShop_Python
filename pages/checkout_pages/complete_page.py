from playwright.async_api import Page, expect

from configs.urls import Urls
from pages.checkout_pages.base_checkout_page import BaseCheckoutPage


class CompletePage(BaseCheckoutPage):
    PAGE_URL: str = Urls.COMPLETE_PAGE
    EXPECTED_COMPLETE_HEADER: str = "Thank you for your order!"
    EXPECTED_COMPLETE_TEXT: str = (
        "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
    )

    def __init__(self, page: Page):
        super().__init__(page)

        self._back_home_button = page.locator("button#back-to-products")
        self._complete_header = page.locator("[data-test='complete-header']")
        self._complete_text = page.locator("[data-test='complete-text']")

    async def click_back_home_button(self) -> None:
        await self._back_home_button.click()

    async def click_cancel(self) -> None:
        await self.click_back_home_button()

    async def check_complete_info_is_valid(self) -> None:
        await expect(self._complete_header).to_have_text(self.EXPECTED_COMPLETE_HEADER)
        await expect(self._complete_text).to_have_text(self.EXPECTED_COMPLETE_TEXT)
