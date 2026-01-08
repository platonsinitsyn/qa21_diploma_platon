import pytest
from core.urls import URLS


@pytest.mark.smoke
def test_check_sections_displayed(logged_in):
    logged_in.check_that_all_sections_displayed()


@pytest.mark.smoke
@pytest.mark.parametrize(
    "title, expected_url, check_page",
    [
        ("Assign Leave", URLS.ASSIGN_LEAVE, "check_assign_leave_page"),
        ("Leave List", URLS.LEAVE, "check_leave_list_page"),
        ("Timesheets", URLS.TIME, "check_timesheets_page"),
        ("Apply Leave", URLS.APPLY_LEAVE, "check_apply_leave_page"),
        ("My Leave", URLS.MY_LEAVE_LIST, "check_my_leave_page"),
        ("My Timesheet", URLS.MY_TIME_TIMESHEET, "check_my_timesheet_page"),
    ],
)
def test_quick_section(logged_in, title, expected_url, check_page):
    logged_in.clisk_on_button(title)
    logged_in.page_should_be_opened(expected_url)
    getattr(logged_in, check_page)()
