from playwright.sync_api import expect
from core.base_page import BasePage
from locators.dashboard_locators import DashboardLocators
from locators.header_locators import HeaderLocators
from locators.assignleave_locators import AssignLeaveLocators
from locators.leavelist_locators import ViewLeaveListLocators
from locators.employeetimesheet_locators import EmployeeTimesheetsLocators
from locators.applyleave_locators import ApplyLeaveLocators
from locators.myleave_locators import MyLeaveLocators
from locators.mytimesheet_locators import MyTimesheetLocators


class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.dashboard_locators = DashboardLocators(page)
        self.header_locators = HeaderLocators(page)
        self.assignleave_locators = AssignLeaveLocators(page)
        self.leavelist_locators = ViewLeaveListLocators(page)
        self.employeetimesheet_locators = EmployeeTimesheetsLocators(page)
        self.applyleave_locators = ApplyLeaveLocators(page)
        self.myleave_locators = MyLeaveLocators(page)
        self.mytimesheet_locators = MyTimesheetLocators(page)

    def clisk_on_button(self, title):
        self.dashboard_locators.get_buttons(title).click()

    def check_quick_assign(self):
        self.dashboard_locators.ASSIGN_LEAVE_BTN.click()

    def check_quick_leave(self):
        self.dashboard_locators.LEAVE_LIST_BTN.click()

    def check_quick_timesheets(self):
        self.dashboard_locators.TIMESHEETS_BTN.click()

    def check_quick_apply(self):
        self.dashboard_locators.APPLY_LEAVE_BTN.click()

    def check_quick_my_leave(self):
        self.dashboard_locators.MY_LEAVE_BTN.click()

    def check_quick_my_timesheet(self):
        self.dashboard_locators.MY_TIMESHEET_BTN.click()

    def check_that_page_opened(self):
        expect(self.dashboard_locators.DASHBOARD_TITLE).to_be_visible()
        expect(self.header_locators.UPGRADE_BUTTON).to_be_visible()
        expect(self.header_locators.USER_DROPDOWN).to_be_visible()

    def check_that_all_sections_displayed(self):
        expect(self.dashboard_locators.TIME_AT_WORK_SECTION).to_be_visible()
        expect(self.dashboard_locators.MY_ACTIONS_SECTION).to_be_visible()
        expect(self.dashboard_locators.QUICK_LAUNCH_SECTION).to_be_visible()
        expect(self.dashboard_locators.BUZZ_POSTS_SECTION).to_be_visible()
        expect(self.dashboard_locators.LEAVE_TODAY_SECTION).to_be_visible()
        expect(self.dashboard_locators.DISTRIBUTION_SECTION_SUBUNIT).to_be_visible()
        expect(self.dashboard_locators.DISTRIBUTION_SECTION_LOCATION).to_be_visible()

    def check_assign_leave_page(self):
        expect(self.assignleave_locators.ASSIGN_LEAVE_TITLE).to_be_visible()

    def check_leave_list_page(self):
        expect(self.leavelist_locators.LEAVE_LIST_TITLE).to_be_visible()

    def check_timesheets_page(self):
        expect(self.employeetimesheet_locators.EMPLOYEE_TIMESHEETS_TITLE).to_be_visible()
        expect(self.employeetimesheet_locators.TIMESHEETS_PENDING_TITLE).to_be_visible()

    def check_apply_leave_page(self):
        expect(self.applyleave_locators.APPLY_LEAVE_TITLE).to_be_visible()

    def check_my_leave_page(self):
        expect(self.myleave_locators.MY_LEAVE_LIST_TITLE).to_be_visible()

    def check_my_timesheet_page(self):
        expect(self.mytimesheet_locators.MY_TIMESHEET_TITLE).to_be_visible()
