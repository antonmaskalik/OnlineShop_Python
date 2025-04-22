import random

import pytest
from faker import Faker
from playwright.async_api import Page, expect

from pages.cart_page import CartPage
from pages.checkout_pages.complete_page import CompletePage
from pages.checkout_pages.overview_page import OverviewPage
from pages.checkout_pages.your_information_page import YourInformationPage
from pages.inventory_page import ProductsPage
from pages.login_page import LoginPage
from pages.models.product_card import ProductCardModel
from test_data.users import STANDARD_USER


class TestOrderProducts:
    @pytest.fixture
    async def test_setup(self, page: Page) -> tuple[CartPage, ProductCardModel]:
        login_page = LoginPage(page)
        products_page = ProductsPage(page)
        await login_page.open()
        await login_page.login(STANDARD_USER)
        product_card = random.choice(await products_page.get_all_product_cards())
        product_card_model = await product_card.to_model()
        await product_card.click_action_button()
        await products_page.header.open_cart()
        return CartPage(page), product_card_model

    async def test_product_added_to_cart(
        self, test_setup: tuple[CartPage, ProductCardModel]
    ):
        cart_page, expected_card = test_setup
        await cart_page.check_page_opened()
        await expect(cart_page._cart_item).to_have_count(1)

        added_products = await cart_page.get_card_models()
        assert (
            expected_card == added_products[0]
        ), "Product in cart does not match the selected product."

    async def test_order_product(self, test_setup: tuple[CartPage, ProductCardModel]):
        cart_page, added_product = test_setup
        your_info_page = YourInformationPage(cart_page.page)
        overview_page = OverviewPage(cart_page.page)
        complete_page = CompletePage(cart_page.page)
        products_page = ProductsPage(cart_page.page)
        fake = Faker()

        await cart_page._checkout_button.click()
        await your_info_page.check_page_opened()
        await your_info_page.fill_form(
            fake.first_name(), fake.last_name(), fake.zipcode()
        )

        await your_info_page.click_continue()
        await overview_page.check_page_opened()
        await overview_page.check_overview_info_visible(added_product)

        await overview_page.click_finish_button()
        await complete_page.check_page_opened()
        await complete_page.check_complete_info_is_valid()

        await complete_page.click_back_home_button()
        await products_page.check_page_opened()
