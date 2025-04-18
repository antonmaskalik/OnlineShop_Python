from playwright.sync_api import Page

from configs.urls import Urls
from pages.base_page import BasePage
from pages.components.product_card import ProductCardComponent


class CartPage(BasePage):
    PAGE_URL = Urls.CART_PAGE

    def __init__(self, page: Page):
        super().__init__(page)

        self._cart_item = page.locator("div.cart_item")
        self._continue_shopping_button = page.locator("button#continue-shopping")
        self._checkout_button = page.locator("button#checkout")

    def get_cart_items(self) -> list[ProductCardComponent]:
        product_cards = self._cart_item
        return [
            ProductCardComponent(product_cards.nth(i))
            for i in range(product_cards.count())
        ]
