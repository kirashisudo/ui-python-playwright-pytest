from src.ui.helper.urls import LOGIN_PASSWORD, LOGIN_USERNAME


class TestLoginPage:
    def test_successful_login(self, login_page):
        login_page.open()
        login_page.open_login_form()
        login_page.login(LOGIN_USERNAME, LOGIN_PASSWORD)
        login_page.check_logged_in_user(LOGIN_USERNAME)
