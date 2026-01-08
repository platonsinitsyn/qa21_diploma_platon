import pytest
from core.urls import URLS


@pytest.mark.smoke
def test_check_upgrade_button(logged_in, header_page):
    header_page.click_upgrade()
    header_page.switch_to_new_tab()
    header_page.page_should_be_opened(URLS.UPGRADE)
    header_page.check_upgrade_is_opened()


@pytest.mark.smoke
def test_check_about_modal(logged_in, header_page):
    header_page.open_modal()
    header_page.check_modal_is_opened()


@pytest.mark.smoke
def test_support_button(logged_in, header_page):
    header_page.click_support()
    logged_in.page_should_be_opened(URLS.SUPPORT)
    header_page.check_support_is_opened()


@pytest.mark.smoke
def test_check_logout(logged_in, header_page, login_object):
    header_page.click_logout()
    logged_in.page_should_be_opened(URLS.LOGIN)
    login_object.check_logout_page()
