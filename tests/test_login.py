import pytest


@pytest.mark.smoke
def test_open_login_page(login_object, open_page):
    login_object.check_that_page_opened(
        title="Login",
        credits="Username : AdminPassword : admin123",
        os_number="OrangeHRM OS 5.8",
        license_text="© 2005 - 2026 OrangeHRM, Inc. All rights reserved.",
    )


@pytest.mark.smoke
def test_positive_login(login_object, dashboard_page, open_page):
    login_object.login("Admin", "admin123")
    dashboard_page.check_that_page_opened()


@pytest.mark.smoke
@pytest.mark.parametrize(
    "user, password, expect",
    [
        ("incorrectUser", "admin123", "Invalid credentials"),
        ("Admin", "incorrectPassword", "Invalid credentials"),
    ],
)
def test_login_validation(login_object, open_page, user, password, expect):
    login_object.login(user, password)
    login_object.check_that_error_is_visible(expect)
