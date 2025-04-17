from playwright.sync_api import Page, expect

from configs.urls import Urls


class BasePage:
    PAGE_URL = Urls.LOGIN_PAGE

    def __init__(self, page: Page):
        self.page = page

    def open(self) -> None:
        self.page.goto(self.PAGE_URL)

    def expect_page_opened(self) -> None:
        expect(self.page).to_have_url(self.PAGE_URL)
