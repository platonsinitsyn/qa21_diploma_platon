import pytest

from core.urls import URLS


@pytest.mark.smoke
def test_check_upgrade_button(logged_in, header_object):
    header_object.click_upgrade()
    header_object.switch_to_new_tab()
    header_object.page_should_be_opened(URLS.UPGRADE)


@pytest.mark.smoke
def test_check_about_modal(logged_in, header_object):
    header_object.check_about_modal()


@pytest.mark.smoke
def test_support_button(logged_in, header_object):
    header_object.click_support()
    logged_in.page_should_be_opened(URLS.SUPPORT)


# @pytest.mark.smoke
# def test_support_button(logged_in, header_object):
#     header_object.click_change_password()
#     logged_in.page_should_be_opened(URLS.CHANGE_PASSWORD)


@pytest.mark.smoke
def test_check_logout(logged_in, header_object):
    header_object.click_logout()
    logged_in.page_should_be_opened(URLS.LOGIN)
