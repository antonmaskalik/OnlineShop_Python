from playwright.async_api import Locator


class BaseComponen:
    def __init__(self, parent_element: Locator):
        self.parent_element = parent_element
