from playwright.sync_api import Locator

from enums.menu_item import MenuItem
from pages.components.base_component import BaseComponen


class MenuContainerComponent(BaseComponen):

    def __init__(self, locator: Locator):
        super().__init__(locator)

        self._menu_items_locator = ".bm-menu .bm-item-list .bm-item"
        self._close_button_locator = "#react-burger-cross-btn"

    def get_menu_items(self) -> list[str]:
        return self._get_menu_item_locator().all_inner_texts()

    def close_menu(self) -> None:
        self.locator.locator(self._close_button_locator).click()

    def click_menu_item(self, item_name: MenuItem) -> None:
        menu_items = self._get_menu_item_locator().all()
        for item in menu_items:
            if item.inner_text() == item_name.value:
                item.click()
                break
        else:
            raise ValueError(f"Menu item '{item_name}' not found.")

    def _get_menu_item_locator(self) -> Locator:
        return self.locator.locator(self._menu_items_locator)
