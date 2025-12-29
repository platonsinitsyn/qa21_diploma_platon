import pytest
from pageobject.dashboard_page import DashboardPage
from pageobject.header_object import HeaderObject
from pageobject.login_page import LoginPage


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


@pytest.fixture()
def logged_in(login_page, dashboard_page, open_page):
    login_page.login("Admin", "admin123")
    dashboard_page.check_that_page_opened()
    return dashboard_page
