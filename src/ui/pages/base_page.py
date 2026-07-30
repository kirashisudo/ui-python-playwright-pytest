from playwright.sync_api import Page
from src.ui.helper.urls import BASE_URL
from playwright.sync_api import expect

class BasePage:
    """Логика тестов на главной"""

    def __init__(self, page: Page, url: str = BASE_URL):
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
        cards = self.page.locator(".card-block")
        expect(cards).to_have_count(number_of_cards)

    def switching_to_phones(self):
        """Переход в раздел Phones"""
        self.page.get_by_text("Phones").click()
        self.page.get_by_role("link", name="Samsung galaxy s6").wait_for()

    def open_product(self, product_name: str) -> None:
        """Открывает карточку товара по его названию."""
        self.page.get_by_role("link", name=product_name).click()

    def check_product_details(self, product_name: str, price: str) -> None:
        """Проверяет основные данные в открытой карточке товара."""
        expect(self.page.locator(".name")).to_have_text(product_name)
        expect(self.page.locator(".price-container")).to_contain_text(price)
        expect(self.page.locator("#more-information")).to_be_visible()
