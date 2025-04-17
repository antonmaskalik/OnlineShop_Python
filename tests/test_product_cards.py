import random

import pytest
from playwright.sync_api import Page, expect

from pages.inventory_page import ProductsPage
from pages.login_page import LoginPage
from test_data.users import STANDARD_USER


class TestProductCards:

    @pytest.fixture
    def test_setup(self, page: Page) -> ProductsPage:
        login_page = LoginPage(page)
        login_page.open()
        login_page.enter_username(STANDARD_USER.username)
        login_page.enter_password(STANDARD_USER.password)
        login_page.click_login()
        return ProductsPage(page)

    def test_product_cards_count(self, test_setup: ProductsPage):
        products_page = test_setup
        all_products = products_page.get_all_product_cards()

        assert len(all_products) >= 6, "Expected >= 6 product cards on the page."
        products_page.expect_all_cards_valid()

    def test_open_product_card(self, test_setup: ProductsPage):
        products_page = test_setup
        product_card = random.choice(products_page.get_all_product_cards())
        product_card.click_on_title()

        assert (
            products_page.PAGE_URL != products_page.page.url
        ), "Product page did not open."
