from playwright.sync_api import expect

from core.base_page import BasePage
from locators.sidebar_locators import SidebarLocators
from locators.mainpage_locators import MainPageLocators
from locators.admin_locators import AdminLocators
from locators.pim_locators import PimLocators
from locators.leavelist_locators import ViewLeaveListLocators
from locators.employeetimesheet_locators import EmployeeTimesheetsLocators
from locators.myinfo_locators import MyInfoLocators
from locators.performance_locators import PerformanceLocators
from locators.recruitment_locators import RecruitmentLocators
from locators.dashboard_locators import DashboardLocators
from locators.directory_locators import DirectoryLocators
from locators.claim_locators import ClaimLocators
from locators.buzz_locators import BuzzLocators


class SidebarObject(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.sidebar_locators = SidebarLocators(page)
        self.mainpage_locators = MainPageLocators(page)
        self.admin_locators = AdminLocators(page)
        self.pim_locators = PimLocators(page)
        self.leavelist_locators = ViewLeaveListLocators(page)
        self.employeetimesheet_locators = EmployeeTimesheetsLocators(page)
        self.myinfo_locators = MyInfoLocators(page)
        self.performance_locators = PerformanceLocators(page)
        self.recruitment_locators = RecruitmentLocators(page)
        self.dashboard_locators = DashboardLocators(page)
        self.directory_locators = DirectoryLocators(page)
        self.claim_locators = ClaimLocators(page)
        self.buzz_locators = BuzzLocators(page)

    def click_on_sidebar_tab(self, title: str):
        tab = self.page.locator("aside").get_by_text(title, exact=True)
        expect(tab).to_be_visible()
        tab.click()

    def click_banner_logo(self):
        self.sidebar_locators.BANNER.click()

    def click_admin_tab(self):
        self.sidebar_locators.ADMIN.click()

    def click_pim_tab(self):
        self.sidebar_locators.PIM.click()

    def click_leave_tab(self):
        self.sidebar_locators.LEAVE.click()

    def click_time_tab(self):
        self.sidebar_locators.TIME.click()

    def click_recruitment_tab(self):
        self.sidebar_locators.RECRUITMENT.click()

    def click_my_info_tab(self):
        self.sidebar_locators.MY_INFO.click()

    def click_performance_tab(self):
        self.sidebar_locators.PERFORMANCE.click()

    def click_dashboard_tab(self):
        self.sidebar_locators.DASHBOARD.click()

    def click_directory_tab(self):
        self.sidebar_locators.DIRECTORY.click()

    def click_claim_tab(self):
        self.sidebar_locators.CLAIM.click()

    def click_buzz_tab(self):
        self.sidebar_locators.BUZZ.click()

    def check_search_results(self, expected_locator):
        expect(expected_locator).to_be_visible()

    def check_search_with_positive_cases(self, search_value):
        self.sidebar_locators.SEARCH.fill(search_value)  # Exact value / "Dashboard"
        self.check_search_results(self.sidebar_locators.DASHBOARD)
        self.sidebar_locators.SEARCH.clear()
        self.sidebar_locators.SEARCH.fill(search_value)  # Partial match / "Dir"
        self.check_search_results(self.sidebar_locators.DIRECTORY)
        self.sidebar_locators.SEARCH.clear()
        self.sidebar_locators.SEARCH.fill(search_value)  # Case validation / "AdMiN"
        self.check_search_results(self.sidebar_locators.ADMIN)
        self.sidebar_locators.SEARCH.clear()

    def check_that_page_opened(self):
        expect(self.sidebar_locators.BANNER).to_be_visible()

    def check_sidebar_menu(self):
        expect(self.sidebar_locators.BANNER).to_be_visible()
        expect(self.sidebar_locators.SEARCH).to_be_visible()
        expect(self.sidebar_locators.SIDEBAR_TOGGLE).to_be_visible()
        expect(self.sidebar_locators.ADMIN).to_be_visible()
        expect(self.sidebar_locators.PIM).to_be_visible()
        expect(self.sidebar_locators.LEAVE).to_be_visible()
        expect(self.sidebar_locators.TIME).to_be_visible()
        expect(self.sidebar_locators.RECRUITMENT).to_be_visible()
        expect(self.sidebar_locators.MY_INFO).to_be_visible()
        expect(self.sidebar_locators.PERFORMANCE).to_be_visible()
        expect(self.sidebar_locators.DASHBOARD).to_be_visible()
        expect(self.sidebar_locators.DIRECTORY).to_be_visible()
        expect(self.sidebar_locators.MAINTENANCE).to_be_visible()
        expect(self.sidebar_locators.CLAIM).to_be_visible()
        expect(self.sidebar_locators.BUZZ).to_be_visible()

    def check_main_page(self):
        expect(self.mainpage_locators.MAIN_PAGE_TITLE).to_be_visible()

    def check_admin_page(self):
        expect(self.admin_locators.ADMIN_TITLE).to_be_visible()

    def check_pim_page(self):
        expect(self.pim_locators.PIM_TITLE).to_be_visible()

    def check_leave_page(self):
        expect(self.leavelist_locators.LEAVE_LIST_TITLE).to_be_visible()

    def check_time_page(self):
        expect(self.employeetimesheet_locators.EMPLOYEE_TIMESHEETS_TITLE).to_be_visible()
        expect(self.employeetimesheet_locators.TIMESHEETS_PENDING_TITLE).to_be_visible()

    def check_recruitment_page(self):
        expect(self.recruitment_locators.RECRUITMENT_TITLE).to_be_visible()

    def check_my_info_page(self):
        expect(self.myinfo_locators.PERSONAL_DETAILS_TAB).to_be_visible()

    def check_performance_page(self):
        expect(self.performance_locators.PERFORMANCE_TITLE).to_be_visible()

    def check_dashboard_page(self):
        expect(self.dashboard_locators.DASHBOARD_TITLE).to_be_visible()

    def check_directory_page(self):
        expect(self.directory_locators.DIRECTORY_TITLE).to_be_visible()

    def check_claim_page(self):
        expect(self.claim_locators.EMPLOYEE_CLAIMS_TITLE).to_be_visible()

    def check_buzz_page(self):
        expect(self.buzz_locators.BUZZ_TITLE).to_be_visible()
