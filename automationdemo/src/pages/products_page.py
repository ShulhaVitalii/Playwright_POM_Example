from playwright.sync_api import Page


class ProductListPage:

    def __init__(self, page: Page):
        self.page = page
        self._products_header = page.locator("span.title")
        self._burger_menu = page.get_by_text("Open Menu")
        self._logout_line = page.get_by_text("Logout")

    @property
    def product_header(self):
        return self._products_header

    def click_on_burger_menu_button(self):
        self._burger_menu.click()

    def click_logout(self):
        self._logout_line.click()

    def do_logout(self):
        self.click_on_burger_menu_button()
        self.click_logout()


