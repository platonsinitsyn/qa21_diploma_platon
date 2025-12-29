import pytest
from core.urls import URLS


@pytest.mark.smoke
def test_check_sections_displayed(logged_in):
    logged_in.check_that_all_sections_displayed()


@pytest.mark.smoke
@pytest.mark.parametrize(
    "title, expected_url",
    [
        ("Assign Leave", URLS.ASSIGN_LEAVE),
        ("Leave List", URLS.LEAVE),
        ("Timesheets", URLS.TIME),
        ("Apply Leave", URLS.APPLY_LEAVE),
        ("My Leave", URLS.MY_LEAVE_LIST),
        ("My Timesheet", URLS.MY_TIME_TIMESHEET),
    ],
)
def test_quick_section(logged_in, title, expected_url):
    logged_in.clisk_on_button(title)
    logged_in.page_should_be_opened(expected_url)
