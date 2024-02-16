from playwright.sync_api import Page

from automationdemo.src.pages.products_page import ProductListPage


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_btn = page.get_by_text("Login")
        self._error_message = page.locator("//h3[@data-test='error']")

    def fill_login_fields(self, username=None, password=None):
        if username:
            self._username.clear()
            self._username.fill(username)
        if password:
            self._password.clear()
            self._password.fill(password)

    def click_login(self):
        self._login_btn.click()

    def do_login(self, username, password):
        self.fill_login_fields(username, password)
        self.click_login()
        return ProductListPage(self.page)

    @property
    def get_error(self):
        return self._error_message

    @property
    def login_button(self):
        return self._login_btn


