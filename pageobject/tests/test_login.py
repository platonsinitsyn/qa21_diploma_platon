import pytest

from pageobject.objects.dashboard_page import DashboardPage
from pageobject.objects.login_page import LoginPage


@pytest.fixture()
def login_page(page):
    return LoginPage(page)


@pytest.fixture()
def dashboard_page(page):
    return DashboardPage(page)


@pytest.fixture()
def open_page(login_page):
    login_page.open_page()


@pytest.mark.smoke
def test_open_login_page(login_page, open_page):
    login_page.check_that_page_opened(
        title="Login",
        credits="Username : AdminPassword : admin123",
        os_number="OrangeHRM OS 5.7",
        license_text="© 2005 - 2025 OrangeHRM, Inc. All rights reserved.",
    )


@pytest.mark.smoke
def test_positive_login(login_page, dashboard_page, open_page):
    login_page.login("Admin", "admin123")
    dashboard_page.check_that_page_opened()


@pytest.mark.smoke
@pytest.mark.parametrize(
    "user, password, expect",
    [
        ("incorrectUser", "admin123", "Invalid credentials"),
        ("Admin", "incorrectPassword", "Invalid credentials"),
    ],
)
def test_login_validation(login_page, open_page, user, password, expect):
    login_page.login(user, password)
    login_page.check_that_error_is_visible(expect)
