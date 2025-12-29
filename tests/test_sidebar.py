import pytest

from core.urls import URLS
from pageobject.sidebar_object import SidebarObject


@pytest.fixture()
def sidebar_object(page):
    return SidebarObject(page)


@pytest.mark.smoke
def test_check_sidebar_menu(logged_in, sidebar_object):
    sidebar_object.check_sidebar_menu()


@pytest.mark.smoke
@pytest.mark.parametrize(
    "title, expected_url",
    [
        ("Banner", URLS.MAIN_PAGE),
        ("Admin", URLS.ADMIN),
        ("PIM", URLS.PIM),
        ("Leave", URLS.LEAVE),
        ("Time", URLS.TIME),
        ("Recruitment", URLS.RECRUITMENT),
        ("My Info", URLS.MY_INFO),
        ("Performance", URLS.PERFORMANCE),
        ("Dashboard", URLS.DASHBOARD),
        ("Directory", URLS.DIRECTORY),
        ("Claim", URLS.CLAIM),
        ("Buzz", URLS.BUZZ),
    ],
)
def test_navigates_to_sidebar_tabs(logged_in, sidebar_object, title, expected_url):
    logged_in.clisk_on_button(title)
    logged_in.page_should_be_opened(expected_url)
