import pytest

from pageobject_structure.pageobject.dashboard_page import DashboardPage
from pageobject_structure.pageobject.login_page import LoginPage


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def dashboard_page(driver):
    return DashboardPage(driver)


@pytest.fixture()
def open_page(login_page):
    login_page.open_page()


@pytest.mark.smoke
def test_open_login_page(login_page, open_page):
    login_page.check_that_page_opened(
        title="Login",
        credits="Username : Admin\nPassword : admin123",
        os_number="OrangeHRM OS 5.7",
        license_text="© 2005 - 2025 OrangeHRM, Inc. All rights reserved.",
    )


@pytest.mark.smoke
def test_positive_login(login_page, dashboard_page, open_page):
    login_page.login("Admin", "admin123")
    dashboard_page.check_that_page_opened("Dashboard")


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
