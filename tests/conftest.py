import pytest
from pages.login_page import LoginPage
from pages.secure_page import SecurePage


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def logged_in(page):
    """Logs in once and returns the secure page, ready for tests."""
    lp = LoginPage(page)
    lp.goto()
    lp.login("tomsmith", "SuperSecretPassword!")
    return SecurePage(page)
