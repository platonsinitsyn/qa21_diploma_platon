import pytest

from pageobject.objects.dashboard_page import DashboardPage
from pageobject.objects.login_page import LoginPage
from pageobject.urls import URLS


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
def test_check_sections_displayed(login_page, dashboard_page, open_page):
    login_page.login("Admin", "admin123")
    dashboard_page.check_that_page_opened()
    dashboard_page.check_that_all_sections_displayed()


@pytest.mark.smoke
@pytest.mark.parametrize(
    "action_method, expected_url",
    [
        ("check_quick_assign", URLS.BASE + URLS.ASSIGN_LEAVE),
        ("check_quick_leave", URLS.BASE + URLS.LEAVE),
        ("check_quick_timesheets", URLS.BASE + URLS.TIME),
        ("check_quick_apply", URLS.BASE + URLS.APPLY_LEAVE),
        ("check_quick_my_leave", URLS.BASE + URLS.MY_LEAVE_LIST),
        ("check_quick_my_timesheet", URLS.BASE + URLS.MY_TIME_TIMESHEET),
    ],
)
def test_quick_section(login_page, dashboard_page, open_page, action_method, expected_url):
    login_page.login("Admin", "admin123")
    dashboard_page.check_that_page_opened()
    method = getattr(dashboard_page, action_method)
    method()
    dashboard_page.page_should_be_opened(expected_url)
