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

    def check_login_error(self, username: str, password: str, expected_message: str) -> None:
        """Проверяет текст alert при неуспешной авторизации."""
        self.open_login_form()
        with self.page.expect_event("dialog") as dialog_info:
            self.login(username, password)
        dialog = dialog_info.value
        assert expected_message in dialog.message
        dialog.accept()

    def logout(self) -> None:
        """Выходит из учётной записи."""
        self.page.get_by_role("link", name="Log out").click()
        expect(self.page.get_by_role("link", name="Log in")).to_be_visible()

    def open_signup_form(self) -> None:
        """Открывает модальное окно регистрации."""
        self.page.get_by_role("link", name="Sign up").click()
        expect(self.page.locator("#signInModal")).to_be_visible()

    def signup(self, username: str, password: str, expected_message: str) -> None:
        """Регистрирует пользователя и проверяет ответ в alert."""
        self.page.locator("#sign-username").fill(username)
        self.page.locator("#sign-password").fill(password)
        with self.page.expect_event("dialog") as dialog_info:
            self.page.locator("#signInModal").get_by_role("button", name="Sign up").click()
        dialog = dialog_info.value
        assert expected_message in dialog.message
        dialog.accept()
