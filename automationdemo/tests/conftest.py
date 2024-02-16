import pytest
from playwright.sync_api import Page


@pytest.fixture()
def setup_teardown(page) -> Page:
    page.goto("https://www.saucedemo.com/")
    yield page
