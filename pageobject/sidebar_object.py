from playwright.sync_api import expect

from core.base_page import BasePage
from locators.sidebar_locators import SidebarLocators


class SidebarObject(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.sidebar_locators = SidebarLocators(page)

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

    # def click_maintenance_tab(self):
    #     self.sidebar_locators.MAINTENANCE.click()

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
        # self.sidebar_locators.SEARCH.fill(search_value) # No results / "Test"
        # self.sidebar_locators.SEARCH.clear()
        # self.sidebar_locators.SEARCH.fill(search_value) # Multiple matches / "D"
        # self.check_search_results(self.sidebar_locators.ADMIN, self.sidebar_locators.DASHBOARD,
        #                           self.sidebar_locators.DIRECTORY)

    # def check_sidebar_toggle(self):
    #     self.sidebar_locators.SIDEBAR_TOGGLE.click()

    # def check_search_with_negative_cases(self):
    #     self.

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
