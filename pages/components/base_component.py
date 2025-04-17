from playwright.sync_api import Locator


class BaseComponen:
    def __init__(self, locator: Locator):
        self.locator = locator
