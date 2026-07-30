from playwright.sync_api import Page
from src.ui.helper.urls import BASE_URL, CART_URL
from src.ui.pages.base_page import BasePage
from playwright.sync_api import expect


class CartPage(BasePage):
    """Логика работы с корзиной."""

    def __init__(self, page: Page, url: str = CART_URL):
        super().__init__(page, url)

    def switching_to_cart(self):
        """Переход в корзину"""
        self.page.locator("#cartur").click()
        assert CART_URL in self.page.url

    def check_place_order_button(self):
        element = self.page.get_by_role(role="button", name="Place Order")
        expect(element).to_be_visible(visible=True)

    def add_current_product_to_cart(self) -> None:
        """Добавляет открытый товар в корзину и подтверждает системный диалог."""
        with self.page.expect_event("dialog") as dialog_info:
            self.page.get_by_role("link", name="Add to cart").click()
        dialog_info.value.accept()

    def check_product_in_cart(self, product_name: str) -> None:
        """Проверяет, что товар показан в таблице корзины."""
        expect(self.page.locator("#tbodyid")).to_contain_text(product_name)

    def check_products_in_cart(self, product_names: list[str]) -> None:
        """Проверяет наличие нескольких товаров в корзине."""
        for product_name in product_names:
            self.check_product_in_cart(product_name)

    def check_total(self, expected_total: int) -> None:
        """Проверяет итоговую стоимость товаров в корзине."""
        expect(self.page.locator("#totalp")).to_have_text(str(expected_total))

    def remove_product(self, product_name: str) -> None:
        """Удаляет товар из таблицы корзины по названию."""
        product_row = self.page.locator("#tbodyid tr").filter(has_text=product_name)
        product_row.get_by_role("link", name="Delete").click()
        expect(self.page.locator("#tbodyid")).not_to_contain_text(product_name)
