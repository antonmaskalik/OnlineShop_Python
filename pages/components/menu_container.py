from playwright.sync_api import Locator

from enums.menu_item import MenuItem
from pages.components.base_component import BaseComponen


class MenuContainerComponent(BaseComponen):

    def __init__(self, parent_element: Locator):
        super().__init__(parent_element)

        self._menu_items = parent_element.locator(".bm-menu .bm-item-list .bm-item")
        self._close_button = parent_element.locator("#react-burger-cross-btn")

    def get_menu_items(self) -> list[str]:
        return self._menu_items.all_inner_texts()

    def close_menu(self) -> None:
        self._close_button.click()

    def click_menu_item(self, item_name: MenuItem) -> None:
        menu_items = self._menu_items.all()
        for item in menu_items:
            if item.inner_text() == item_name.value:
                item.click()
                break
        else:
            raise ValueError(f"Menu item '{item_name}' not found.")
