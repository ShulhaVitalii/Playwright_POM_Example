from playwright.sync_api import Page, expect
from automationdemo.src.pages.login_page import LoginPage
from automationdemo.src.pages.products_page import ProductListPage


def test_success_login(setup_teardown) -> None:
    page = setup_teardown
    lp = LoginPage(page)

    plp = lp.do_login("standard_user", "secret_sauce")
    products_header = plp.product_header
    expect(products_header).to_have_text("Products")


def test_invalid_login(setup_teardown) -> None:
    page = setup_teardown
    lp = LoginPage(page)

    lp.do_login("invalid_user", "secret_sauce")

    expected_error_message = "Epic sadface: Username and password do not match any user in this service"
    error_message_locator = lp.get_error

    expect(error_message_locator).to_contain_text(expected_error_message)


def test_login_without_credentials(setup_teardown) -> None:
    page = setup_teardown
    lp = LoginPage(page)

    lp.click_login()

    expected_error_message = "Epic sadface: Username is required"
    error_message_locator = lp.get_error

    expect(error_message_locator).to_contain_text(expected_error_message)


def test_success_logout(setup_teardown) -> None:
    page = setup_teardown
    lp = LoginPage(page)

    plp = lp.do_login("standard_user", "secret_sauce")
    plp.do_logout()
    expect(lp.login_button).to_be_visible()


