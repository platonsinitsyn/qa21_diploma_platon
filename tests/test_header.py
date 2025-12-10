import pytest

from core.urls import URLS
from pageobject.objects.dashboard_page import DashboardPage
from pageobject.objects.header_object import HeaderObject
from pageobject.objects.login_page import LoginPage


@pytest.fixture()
def login_page(page):
    return LoginPage(page)


@pytest.fixture()
def dashboard_page(page):
    return DashboardPage(page)


@pytest.fixture()
def header_object(page):
    return HeaderObject(page)


@pytest.fixture()
def open_page(login_page):
    login_page.open_page()


@pytest.mark.smoke
def test_check_upgrade_button(login_page, dashboard_page, open_page, header_object):
    login_page.login("Admin", "admin123")
    dashboard_page.check_that_page_opened()
    header_object.click_upgrade()
    header_object.switch_to_new_tab()
    header_object.page_should_be_opened(URLS.UPGRADE)


@pytest.mark.smoke
def test_check_about_modal(login_page, dashboard_page, open_page, header_object):
    login_page.login("Admin", "admin123")
    dashboard_page.check_that_page_opened()
    header_object.check_about_modal()


@pytest.mark.smoke
def test_support_button(login_page, dashboard_page, open_page, header_object):
    login_page.login("Admin", "admin123")
    dashboard_page.check_that_page_opened()
    header_object.click_support()
    login_page.page_should_be_opened(URLS.BASE + URLS.SUPPORT)


# @pytest.mark.smoke
# def test_support_button(login_page, dashboard_page, open_page, header_object):
#     login_page.login("Admin", "admin123")
#     dashboard_page.check_that_page_opened()
#     header_object.click_change_password()
#     login_page.page_should_be_opened(URLS.BASE + URLS.CHANGE_PASSWORD)


@pytest.mark.smoke
def test_check_logout(login_page, dashboard_page, open_page, header_object):
    login_page.login("Admin", "admin123")
    dashboard_page.check_that_page_opened()
    header_object.click_logout()
    login_page.page_should_be_opened(URLS.BASE + URLS.LOGIN)
