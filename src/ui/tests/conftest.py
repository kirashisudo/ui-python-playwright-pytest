import pytest
from playwright.sync_api import sync_playwright

from src.ui.pages.base_page import BasePage
from src.ui.pages.cart_page import CartPage
from src.ui.pages.login_page import LoginPage


@pytest.fixture
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(channel="msedge", headless=False)
    context = browser.new_context(viewport={"width": 1000, "height": 1019})
    page = context.new_page()
    yield page
    context.close()
    browser.close()
    playwright.stop()

@pytest.fixture
def base_page(page):
    return BasePage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def login_page(page):
    return LoginPage(page)
