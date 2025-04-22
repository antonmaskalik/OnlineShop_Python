import pytest
from playwright.async_api import Page, expect

from pages.inventory_page import ProductsPage
from pages.login_page import LoginPage
from test_data.login_test_data import login_negative_cases
from test_data.users import STANDARD_USER, User


class TestLogin:

    @pytest.fixture
    async def test_setup(self, page: Page) -> tuple[LoginPage, ProductsPage]:
        login_page = LoginPage(page)
        await login_page.open()
        return login_page, ProductsPage(page)

    async def test_login_successful(self, test_setup: tuple[LoginPage, ProductsPage]):
        login_page, products_page = test_setup

        await login_page.check_page_opened()

        await login_page.enter_username(STANDARD_USER.username)
        await login_page.enter_password(STANDARD_USER.password)
        await login_page.click_login()

        await products_page.check_page_opened()

    @pytest.mark.parametrize("user, expected_error", login_negative_cases)
    async def test_login_negative_cases(
        self,
        test_setup: tuple[LoginPage, ProductsPage],
        user: User,
        expected_error: str,
    ):
        login_page, _ = test_setup

        await login_page.enter_username(user.username)
        await login_page.enter_password(password=user.password)
        await login_page.click_login()
        await login_page.chck_error_message(expected_error)
