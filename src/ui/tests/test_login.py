from uuid import uuid4

from src.ui.helper.urls import LOGIN_PASSWORD, LOGIN_USERNAME


class TestLoginPage:
    def test_successful_login(self, login_page):
        login_page.open()
        login_page.open_login_form()
        login_page.login(LOGIN_USERNAME, LOGIN_PASSWORD)
        login_page.check_logged_in_user(LOGIN_USERNAME)

    def test_login_with_invalid_password(self, login_page):
        login_page.open()
        login_page.check_login_error(
            LOGIN_USERNAME,
            "invalid-password",
            "Wrong password.",
        )

    def test_logout(self, login_page):
        login_page.open()
        login_page.open_login_form()
        login_page.login(LOGIN_USERNAME, LOGIN_PASSWORD)
        login_page.check_logged_in_user(LOGIN_USERNAME)
        login_page.logout()

    def test_signup_and_duplicate_username(self, login_page):
        username = f"pw_user_{uuid4().hex[:10]}"
        password = "test-password"

        login_page.open()
        login_page.open_signup_form()
        login_page.signup(username, password, "Sign up successful.")

        login_page.open()
        login_page.open_signup_form()
        login_page.signup(username, password, "This user already exist.")
