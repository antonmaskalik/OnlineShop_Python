from abc import ABC

from playwright.async_api import Page, expect

from configs.urls import Urls
from pages.components.header import HeaderComponent


class BasePage(ABC):
    PAGE_URL: str = Urls.LOGIN_PAGE

    def __init__(self, page: Page):
        self.page = page
        self.header = HeaderComponent(page.locator(".primary_header"))

    async def open(self) -> None:
        await self.page.goto(self.PAGE_URL)

    async def check_page_opened(self) -> None:
        await expect(self.page).to_have_url(self.PAGE_URL)
