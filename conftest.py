import pytest
from pageobject.dashboard_page import DashboardPage
from pageobject.header_object import HeaderObject
from pageobject.login_object import LoginPage
from pageobject.pim_object import PimPage
from pageobject.sidebar_object import SidebarObject


@pytest.fixture()
def login_object(page):
    return LoginPage(page)


@pytest.fixture()
def dashboard_page(page):
    return DashboardPage(page)


@pytest.fixture()
def header_page(page):
    return HeaderObject(page)


@pytest.fixture()
def pim_page(page):
    return PimPage(page)


@pytest.fixture()
def open_page(login_object):
    login_object.open_page()


@pytest.fixture()
def sidebar_object(page):
    return SidebarObject(page)


@pytest.fixture()
def logged_in(login_object, dashboard_page, open_page):
    login_object.login("Admin", "admin123")
    dashboard_page.check_that_page_opened()
    return dashboard_page
