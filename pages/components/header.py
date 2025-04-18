from playwright.sync_api import Locator, expect

from enums.menu_item import MenuItem
from pages.components.base_component import BaseComponen
from pages.components.menu_container import MenuContainerComponent


class HeaderComponent(BaseComponen):
    def __init__(self, parent_element: Locator):
        super().__init__(parent_element)

        self._cart_icon = parent_element.locator("a.shopping_cart_link")
        self._menu_button = parent_element.locator("#react-burger-menu-btn")
        self._logo_locator = parent_element.locator("div.app_logo")

    def open_cart(self) -> None:
        self._cart_icon.click()

    def click_menu_button(self) -> MenuContainerComponent:
        self._menu_button.click()
        return MenuContainerComponent(self.parent_element)

    def select_menu_item(self, item_name: MenuItem) -> None:
        self.click_menu_button().click_menu_item(item_name)

    def check_logo_is_visible(self) -> None:
        expect(self._logo_locator).to_be_visible()
