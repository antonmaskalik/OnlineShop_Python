from playwright.sync_api import Locator

from enums.menu_item import MenuItem
from pages.components.base_component import BaseComponen
from pages.components.menu_container import MenuContainerComponent


class HeaderComponent(BaseComponen):
    def __init__(self, locator: Locator):
        super().__init__(locator)

        self._cart_icon_locator = "a.shopping_cart_link"
        self._menu_button_locator = "#react-burger-menu-btn"
        self._logo_locator = "div.app_logo"

    def open_cart(self) -> None:
        self.locator.locator(self._cart_icon_locator).click()

    def logo(self) -> Locator:
        return self.locator.locator(self._logo_locator)

    def click_menu_button(self) -> MenuContainerComponent:
        self.locator.locator(self._menu_button_locator).click()
        return MenuContainerComponent(self.locator)

    def select_menu_item(self, item_name: MenuItem) -> None:
        self.click_menu_button().click_menu_item(item_name)
