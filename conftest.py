import pytest
from playwright.sync_api import sync_playwright

from units.config import Config

CONFIG = Config()


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        if CONFIG.BROWSER == "chromium":
            browser = p.chromium.launch(headless=CONFIG.HEADLESS)
        elif CONFIG.BROWSER == "firefox":
            browser = p.firefox.launch(headless=CONFIG.HEADLESS)
        elif CONFIG.BROWSER == "webkit":
            browser = p.webkit.launch(headless=CONFIG.HEADLESS)
        else:
            raise ValueError(f"Unsupported browser: {CONFIG.BROWSER}")

        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(viewport=CONFIG.WINDOW_SIZE)
    page = context.new_page()
    yield page
    context.close()
