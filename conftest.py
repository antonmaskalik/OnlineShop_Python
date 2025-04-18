import pytest
from playwright.async_api import async_playwright

from units.config import Config

CONFIG = Config()


@pytest.fixture(scope="function")
async def browser():
    async with async_playwright() as p:
        if CONFIG.BROWSER == "chromium":
            browser = await p.chromium.launch(headless=CONFIG.HEADLESS)
        elif CONFIG.BROWSER == "firefox":
            browser = await p.firefox.launch(headless=CONFIG.HEADLESS)
        elif CONFIG.BROWSER == "webkit":
            browser = await p.webkit.launch(headless=CONFIG.HEADLESS)
        else:
            raise ValueError(f"Unsupported browser: {CONFIG.BROWSER}")

        yield browser
        await browser.close()


@pytest.fixture(scope="function")
async def page(browser):
    context = await browser.new_context(viewport=CONFIG.WINDOW_SIZE)
    page = await context.new_page()
    yield page
    await context.close()
