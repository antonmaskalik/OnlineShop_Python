import random

import pytest
from playwright.async_api import Page, expect

from pages.inventory_page import ProductsPage
from pages.login_page import LoginPage
from test_data.users import STANDARD_USER


class TestProductCards:

    @pytest.fixture
    async def test_setup(self, page: Page) -> ProductsPage:
        login_page = LoginPage(page)
        await login_page.open()
        await login_page.enter_username(STANDARD_USER.username)
        await login_page.enter_password(STANDARD_USER.password)
        await login_page.click_login()
        return ProductsPage(page)

    async def test_product_cards_count(self, test_setup: ProductsPage):
        products_page = test_setup
        all_products = await products_page.get_all_product_cards()

        assert len(all_products) >= 6, "Expected >= 6 product cards on the page."
        await products_page.check_all_cards_valid()

    async def test_open_product_card(self, test_setup: ProductsPage):
        products_page = test_setup
        product_card = random.choice(await products_page.get_all_product_cards())
        await product_card.click_on_title()

        assert (
            products_page.PAGE_URL != products_page.page.url
        ), "Product page did not open."
