from playwright.async_api import Page

from configs.urls import Urls
from pages.base_page import BasePage
from pages.components.product_card import ProductCardComponent
from pages.models.product_card import ProductCardModel


class CartPage(BasePage):
    PAGE_URL: str = Urls.CART_PAGE

    def __init__(self, page: Page):
        super().__init__(page)

        self._cart_item = page.locator("div.cart_item")
        self._continue_shopping_button = page.locator("button#continue-shopping")
        self._checkout_button = page.locator("button#checkout")

    async def get_card_items(self) -> list[ProductCardComponent]:
        product_cards = self._cart_item
        return [
            ProductCardComponent(product_cards.nth(i))
            for i in range(await product_cards.count())
        ]

    async def get_card_models(self) -> list[ProductCardModel]:
        product_cards = await self.get_card_items()
        return [await card.to_model() for card in product_cards]
