from playwright.async_api import Page

from configs.urls import Urls
from pages.base_page import BasePage
from pages.components.product_card import ProductCardComponent
from pages.models.product_card import ProductCardModel


class ProductsPage(BasePage):
    PAGE_URL: str = Urls.PRODUCTS_PAGE

    def __init__(self, page: Page):
        super().__init__(page)

        self._product_card = page.locator(".inventory_item")

    async def get_all_product_cards(self) -> list[ProductCardComponent]:
        product_cards = self._product_card
        return [
            ProductCardComponent(product_cards.nth(i))
            for i in range(await product_cards.count())
        ]

    async def get_card_models(self) -> list[ProductCardModel]:
        product_cards = await self.get_all_product_cards()
        return [await card.to_model() for card in product_cards]

    async def check_all_cards_valid(self) -> None:
        for card in await self.get_all_product_cards():
            await card.check_valid_card()
            await card.check_image_visible()
