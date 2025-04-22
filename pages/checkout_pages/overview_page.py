from playwright.async_api import Page, expect

from configs.urls import Urls
from pages.checkout_pages.base_checkout_page import BaseCheckoutPage
from pages.components.product_card import ProductCardComponent
from pages.models.product_card import ProductCardModel


class OverviewPage(BaseCheckoutPage):
    PAGE_URL: str = Urls.OVERVIEW_PAGE

    def __init__(self, page: Page):
        super().__init__(page)

        self._cart_item = page.locator("div.cart_item")
        self._finish_button = page.locator("button#finish")
        self._payment_info_label = page.locator("[data-test='payment-info-label']")
        self._payment_info_value = page.locator("[data-test='payment-info-value']")
        self._shipping_info_label = page.locator("[data-test='shipping-info-label']")
        self._shipping_info_value = page.locator("[data-test='shipping-info-value']")
        self._total_label = page.locator("[data-test='total-info-label']")
        self._sub_total_label = page.locator("[data-test='subtotal-label']")
        self._tax_label = page.locator("[data-test='tax-label']")
        self._total_label = page.locator("[data-test='total-label']")

    async def get_card_items(self) -> list[ProductCardComponent]:
        product_cards = self._cart_item
        return [
            ProductCardComponent(product_cards.nth(i))
            for i in range(await product_cards.count())
        ]

    async def get_card_models(self) -> list[ProductCardModel]:
        product_cards = await self.get_card_items()
        return [await card.to_model() for card in product_cards]

    async def click_finish_button(self) -> None:
        await self._finish_button.click()

    async def check_overview_info_visible(self, *products: ProductCardModel) -> None:
        product_cards = await self.get_card_items()
        await expect(self._cart_item).to_have_count(len(products))
        for i, product in enumerate(products):
            assert (
                await product_cards[i].to_model() == product
            ), f"Product card {product_cards[i]} does not match expected product {product}."

        await expect(self._payment_info_label).to_be_visible()
        await expect(self._payment_info_value).to_be_visible()
        await expect(self._shipping_info_label).to_be_visible()
        await expect(self._shipping_info_value).to_be_visible()
        await expect(self._total_label).to_be_visible()
        await expect(self._sub_total_label).to_be_visible()
        await expect(self._tax_label).to_be_visible()
        await expect(self._total_label).to_be_visible()
