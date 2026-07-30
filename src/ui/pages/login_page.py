from playwright.sync_api import Page, expect

from src.ui.pages.base_page import BasePage


class LoginPage(BasePage):
    """Логика авторизации пользователя."""

    def open_login_form(self) -> None:
        """Открывает модальное окно входа."""
        self.page.get_by_role("link", name="Log in").click()
        expect(self.page.locator("#logInModal")).to_be_visible()

    def login(self, username: str, password: str) -> None:
        """Заполняет форму входа и отправляет её."""
        self.page.locator("#loginusername").fill(username)
        self.page.locator("#loginpassword").fill(password)
        self.page.locator("#logInModal").get_by_role("button", name="Log in").click()

    def check_logged_in_user(self, username: str) -> None:
        """Проверяет приветствие после успешной авторизации."""
        expect(self.page.locator("#nameofuser")).to_have_text(f"Welcome {username}")
