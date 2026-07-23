from playwright.sync_api import Page
from src.ui.helper.urls import BASE_URL, CART_URL


class BasePage:
    """Логика работы с главной страницей."""

    def __init__(self, page: Page, url=BASE_URL):
        self.page = page
        self.url = url

    def open(self):
        """Открывает страницу."""
        self.page.goto(self.url)

    def switching_to_monitors(self) -> None:
        """Переходит в раздел Monitors."""
        self.page.get_by_text("Monitors").click()
        self.page.get_by_text("Apple monitor 24").wait_for(state="visible")

    def check_cards(self, number_of_cards: int):
        """Проверяет количество карточек товара."""
        monitors = self.page.locator(".card-block")
        cnt = monitors.count()
        assert cnt == number_of_cards

    def switching_to_cart(self):
        self.page.locator("#cartur").click()
        assert CART_URL in self.page.url
