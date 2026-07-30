from abc import ABC
from playwright.sync_api import Page
from playwright.sync_api import expect


class Base(ABC):
    """Базовый класс для взаимодействия с эллементами"""
    def __init__(self, page: Page, strategy: str = None, selector: str = None,
                 role=None, value: str = None):
        self.page = page
        self.strategy = strategy
        self.selector = selector
        self.role = role
        self.value = value

        if strategy == "locator":
            self._element = self.page.locator(self.selector)
        elif strategy == "by_role":
            self._element = self.page.get_by_role(role = self.role, name = self.value)
        elif strategy == "by_text":
            self._element = self.page.get_by_text(text = self.value)
        elif strategy == "by_placeholder":
            self._element = self.page.get_by_placeholder(self.value)
        else:
            raise ValueError("Указана неверная стратегия")

    def click(self):
        """Кликает по элементу"""
        self._element.click()

    def check_visible(self):
        """Проверяет видимость элемента"""
        expect(self._element).to_be_visible(visible=True)

    def wait_for(self, timeout_msec: int = None):
        """Ожидает когда элемент удовлетворяет условию state"""
        self._element.wait_for(state=state, timeout=timeout_msec)