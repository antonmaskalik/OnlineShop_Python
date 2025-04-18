from playwright.sync_api import Locator, expect

from pages.components.base_component import BaseComponen


class ProductCardComponent(BaseComponen):
    def __init__(self, parent_element: Locator):
        super().__init__(parent_element)

        self._card_title = parent_element.locator("[data-test='inventory-item-name']")
        self._card_price = parent_element.locator("[data-test='inventory-item-price']")
        self._card_description = parent_element.locator(
            "[data-test='inventory-item-desc']"
        )
        self._card_image = parent_element.locator("img")
        self._action_button = parent_element.locator("button")

    def click_on_title(self) -> None:
        self._card_title.click()

    def click_action_button(self) -> None:
        self._action_button.click()

    def check_image_visible(self) -> None:
        expect(self._card_image).to_be_visible()

    def check_valid_card(self) -> None:
        expect(self._card_title).to_be_visible()
        expect(self._card_price).to_be_visible()
        expect(self._card_description).to_be_visible()
        expect(self._action_button).to_be_visible()
        expect(self._action_button).to_be_enabled()
