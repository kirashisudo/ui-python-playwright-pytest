from pydoc import pager

import pytest
from playwright.sync_api import sync_playwright

from pages.base_page import BasePage


@pytest.fixture
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(channel="msedge", headless=False)
    context = browser.new_context(viewport={"width": 1000, "height": 1019})
    page = context.new_page()
    yield page
    browser.close()
    playwright.stop()

@pytest.fixture
def base_page(browser):
    return BasePage(browser)