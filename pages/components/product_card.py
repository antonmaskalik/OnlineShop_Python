import re
from functools import total_ordering

from playwright.sync_api import Locator, expect

from pages.components.base_component import BaseComponen


class ProductCardComponent(BaseComponen):
    def __init__(self, locator: Locator):
        super().__init__(locator)

        self._card_title_locator = "[data-test='inventory-item-name']"
        self._card_price_locator = "[data-test='inventory-item-price']"
        self._card_description_locator = "[data-test='inventory-item-desc']"
        self._card_image_locator = "img"
        self._action_button_locator = "button"

    def title(self) -> Locator:
        return self.locator.locator(self._card_title_locator)

    def click_on_title(self) -> None:
        self.locator.locator(self._card_title_locator).click()

    def price(self) -> Locator:
        return self.locator.locator(self._card_price_locator)

    def description(self) -> Locator:
        return self.locator.locator(self._card_description_locator)

    def image(self) -> Locator:
        return self.locator.locator(self._card_image_locator)

    def action_button(self) -> Locator:
        return self.locator.locator(self._action_button_locator)

    def click_action_button(self) -> None:
        self.action_button().click()

    def expect_card_valid(self) -> None:
        expect(self.title()).to_be_visible()
        expect(self.price()).to_be_visible()
        expect(self.description()).to_be_visible()
        expect(self.action_button()).to_be_visible()
        expect(self.action_button()).to_be_enabled()
