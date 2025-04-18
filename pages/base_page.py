from playwright.async_api import Page, expect

from configs.urls import Urls


class BasePage:
    PAGE_URL = Urls.LOGIN_PAGE

    def __init__(self, page: Page):
        self.page = page

    async def open(self) -> None:
        await self.page.goto(self.PAGE_URL)

    async def expect_page_opened(self) -> None:
        await expect(self.page).to_have_url(self.PAGE_URL)
