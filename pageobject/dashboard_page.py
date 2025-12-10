from core.base_page import BasePage
from locators.dashboard_locators import DashboardLocators
from locators.header_locators import HeaderLocators


class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.dashboard_locators = DashboardLocators
        self.header_locators = HeaderLocators

    def check_quick_assign(self):
        self.click(self.dashboard_locators.ASSIGN_LEAVE_BTN)

    def check_quick_leave(self):
        self.click(self.dashboard_locators.LEAVE_LIST_BTN)

    def check_quick_timesheets(self):
        self.click(self.dashboard_locators.TIMESHEETS_BTN)

    def check_quick_apply(self):
        self.click(self.dashboard_locators.APPLY_LEAVE_BTN)

    def check_quick_my_leave(self):
        self.click(self.dashboard_locators.MY_LEAVE_BTN)

    def check_quick_my_timesheet(self):
        self.click(self.dashboard_locators.MY_TIMESHEET_BTN)

    def check_that_page_opened(self):
        self.should_be_visible(self.dashboard_locators.DASHBOARD_TITLE)
        self.should_be_visible(self.header_locators.UPGRADE_BUTTON)
        self.should_be_visible(self.header_locators.USER_DROPDOWN)

    def check_that_all_sections_displayed(self):
        self.should_be_visible(self.dashboard_locators.TIME_AT_WORK_SECTION)
        self.should_be_visible(self.dashboard_locators.MY_ACTIONS_SECTION)
        self.should_be_visible(self.dashboard_locators.QUICK_LAUNCH_SECTION)
        self.should_be_visible(self.dashboard_locators.BUZZ_POSTS_SECTION)
        self.should_be_visible(self.dashboard_locators.LEAVE_TODAY_SECTION)
        self.should_be_visible(self.dashboard_locators.DISTRIBUTION_SECTION_SUBUNIT)
        self.should_be_visible(self.dashboard_locators.DISTRIBUTION_SECTION_LOCATION)
