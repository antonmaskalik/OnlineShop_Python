import pytest
from playwright.sync_api import Page, expect

from pages.inventory_page import ProductsPage
from pages.login_page import LoginPage
from test_data.login_test_data import login_negative_cases
from test_data.users import STANDARD_USER, User


class TestLogin:

    @pytest.fixture
    def test_setup(self, page: Page) -> tuple[LoginPage, ProductsPage]:
        login_page = LoginPage(page)
        login_page.open()
        return login_page, ProductsPage(page)

    def test_login_successful(self, test_setup: tuple[LoginPage, ProductsPage]):
        login_page, products_page = test_setup

        login_page.expect_page_opened()

        login_page.enter_username(STANDARD_USER.username)
        login_page.enter_password(STANDARD_USER.password)
        login_page.click_login()

        products_page.expect_page_opened()

    @pytest.mark.parametrize("user, expected_error", login_negative_cases)
    def test_login_negative_cases(
        self,
        test_setup: tuple[LoginPage, ProductsPage],
        user: User,
        expected_error: str,
    ):
        login_page, _ = test_setup

        login_page.enter_username(user.username)
        login_page.enter_password(password=user.password)
        login_page.click_login()
        error_message = login_page.get_error_message()

        expect(error_message).to_be_visible()
        expect(error_message).to_have_text(expected_error)
