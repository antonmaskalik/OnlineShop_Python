from playwright.sync_api import Page, expect

from configs.urls import Urls
from pages.base_page import BasePage
from pages.components.product_card import ProductCardComponent


class ProductsPage(BasePage):
    PAGE_URL = Urls.PRODUCTS_PAGE

    def __init__(self, page: Page):
        super().__init__(page)

        self._product_card_locator = ".inventory_item"

    def get_all_product_cards(self) -> list[ProductCardComponent]:
        product_cards = self.page.locator(self._product_card_locator)
        return [
            ProductCardComponent(product_cards.nth(i))
            for i in range(product_cards.count())
        ]

    def expect_all_cards_valid(self) -> None:
        for card in self.get_all_product_cards():
            card.expect_card_valid()
            expect(card.image()).to_be_visible()
