from playwright.async_api import Locator, expect

from enums.menu_item import MenuItem
from pages.components.base_component import BaseComponen
from pages.components.menu_container import MenuContainerComponent


class HeaderComponent(BaseComponen):
    def __init__(self, parent_element: Locator):
        super().__init__(parent_element)

        self._cart_icon = parent_element.locator("a.shopping_cart_link")
        self._menu_button = parent_element.locator("#react-burger-menu-btn")
        self._logo_locator = parent_element.locator("div.app_logo")

    async def open_cart(self) -> None:
        await self._cart_icon.click()

    async def click_menu_button(self) -> MenuContainerComponent:
        await self._menu_button.click()
        return MenuContainerComponent(self.parent_element)

    async def select_menu_item(self, item_name: MenuItem) -> None:
        menu_container = await self.click_menu_button()
        await menu_container.click_menu_item(item_name)

    async def check_logo_is_visible(self) -> None:
        await expect(self._logo_locator).to_be_visible()
