import pytest
from core.urls import URLS


@pytest.mark.smoke
def test_check_sidebar_menu(logged_in, sidebar_object):
    sidebar_object.check_sidebar_menu()


@pytest.mark.smoke
@pytest.mark.parametrize(
    "title, expected_url, check_page",
    [
        ("Admin", URLS.ADMIN, "check_admin_page"),
        ("PIM", URLS.PIM, "check_pim_page"),
        ("Leave", URLS.LEAVE, "check_leave_page"),
        ("Time", URLS.TIME, "check_time_page"),
        ("Recruitment", URLS.RECRUITMENT, "check_recruitment_page"),
        ("My Info", URLS.MY_INFO, "check_my_info_page"),
        ("Performance", URLS.PERFORMANCE, "check_performance_page"),
        ("Dashboard", URLS.DASHBOARD, "check_dashboard_page"),
        ("Directory", URLS.DIRECTORY, "check_directory_page"),
        ("Claim", URLS.CLAIM, "check_claim_page"),
        ("Buzz", URLS.BUZZ, "check_buzz_page"),
    ],
)
def test_navigates_to_sidebar_tabs(logged_in, sidebar_object, title, expected_url, check_page):
    sidebar_object.click_on_sidebar_tab(title)
    sidebar_object.page_should_be_opened(expected_url)
    getattr(sidebar_object, check_page)()
