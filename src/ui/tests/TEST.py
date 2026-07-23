from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

import src.ui.pages.base_page
from pages import base_page
from src.ui.pages.base_page import BasePage

def test(base_page):
    base_page.open()
    base_page.switching_to_monitors()
    base_page.check_cards(2)

def test2(base_page):
    base_page.open()
    base_page.switching_to_cart()
