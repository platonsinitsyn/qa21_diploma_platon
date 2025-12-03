import pytest

from pageobject_structure.pageobject.dashboard_page import DashboardPage
from pageobject_structure.pageobject.login_page import LoginPage
from pageobject_structure.pageobject.sidebar_object import SidebarObject
from pageobject_structure.urls import URLS


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def dashboard_page(driver):
    return DashboardPage(driver)


@pytest.fixture()
def sidebar_object(driver):
    return SidebarObject(driver)


@pytest.fixture()
def open_page(login_page):
    login_page.open_page()


@pytest.mark.smoke
def test_check_sidebar_menu(login_page, dashboard_page, open_page, sidebar_object):
    login_page.login("Admin", "admin123")
    dashboard_page.check_that_page_opened("Dashboard")
    sidebar_object.check_sidebar_menu()


@pytest.mark.smoke
@pytest.mark.parametrize(
    "click_tab, expected_url",
    [
        ("click_banner_logo", URLS.MAIN_PAGE),
        ("click_admin_tab", URLS.BASE + URLS.ADMIN),
        ("click_pim_tab", URLS.BASE + URLS.PIM),
        ("click_leave_tab", URLS.BASE + URLS.LEAVE),
        ("click_time_tab", URLS.BASE + URLS.TIME),
        ("click_recruitment_tab", URLS.BASE + URLS.RECRUITMENT),
        ("click_my_info_tab", URLS.BASE + URLS.MY_INFO),
        ("click_performance_tab", URLS.BASE + URLS.PERFORMANCE),
        ("click_dashboard_tab", URLS.BASE + URLS.DASHBOARD),
        ("click_directory_tab", URLS.BASE + URLS.DIRECTORY),
        ("click_claim_tab", URLS.BASE + URLS.CLAIM),
        ("click_buzz_tab", URLS.BASE + URLS.BUZZ),
    ],
)
def test_navigates_to_sidebar_tabs(login_page, dashboard_page, open_page, click_tab, expected_url, sidebar_object):
    login_page.login("Admin", "admin123")
    dashboard_page.check_that_page_opened("Dashboard")
    page = getattr(sidebar_object, click_tab)
    page()
    sidebar_object.page_should_be_opened(expected_url)
