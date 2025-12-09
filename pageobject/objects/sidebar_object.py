from pageobject.core.base_page import BasePage
from pageobject.locators.sidebar_locators import SidebarLocators


class SidebarObject(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.sidebar_locators = SidebarLocators

    def click_banner_logo(self):
        self.click(self.sidebar_locators.BANNER)

    def click_admin_tab(self):
        self.click(self.sidebar_locators.ADMIN)

    def click_pim_tab(self):
        self.click(self.sidebar_locators.PIM)

    def click_leave_tab(self):
        self.click(self.sidebar_locators.LEAVE)

    def click_time_tab(self):
        self.click(self.sidebar_locators.TIME)

    def click_recruitment_tab(self):
        self.click(self.sidebar_locators.RECRUITMENT)

    def click_my_info_tab(self):
        self.click(self.sidebar_locators.MY_INFO)

    def click_performance_tab(self):
        self.click(self.sidebar_locators.PERFORMANCE)

    def click_dashboard_tab(self):
        self.click(self.sidebar_locators.DASHBOARD)

    def click_directory_tab(self):
        self.click(self.sidebar_locators.DIRECTORY)

    def click_claim_tab(self):
        self.click(self.sidebar_locators.CLAIM)

    def click_buzz_tab(self):
        self.click(self.sidebar_locators.BUZZ)

    # def click_maintenance_tab(self):
    #     self.click(self.sidebar_locators.MAINTENANCE)

    def check_search_results(self, expected_visible):
        all_items = [
            self.sidebar_locators.ADMIN,
            self.sidebar_locators.PIM,
            self.sidebar_locators.LEAVE,
            self.sidebar_locators.TIME,
            self.sidebar_locators.RECRUITMENT,
            self.sidebar_locators.MY_INFO,
            self.sidebar_locators.PERFORMANCE,
            self.sidebar_locators.DASHBOARD,
            self.sidebar_locators.DIRECTORY,
            self.sidebar_locators.MAINTENANCE,
            self.sidebar_locators.CLAIM,
            self.sidebar_locators.BUZZ,
        ]

        for item in all_items:
            if item == expected_visible:
                self.should_be_visible(item)
            else:
                self.should_be_not_visible(item)

    def check_search_with_positive_cases(self, search_value):
        self.fill(self.sidebar_locators.SEARCH, text=search_value)  # Exact value / "Dashboard"
        self.check_search_results(self.sidebar_locators.DASHBOARD)
        self.driver.find_element(*self.sidebar_locators.SEARCH).clear()
        self.fill(self.sidebar_locators.SEARCH, text=search_value)  # Partial match / "Dir"
        self.check_search_results(self.sidebar_locators.DIRECTORY)
        self.driver.find_element(*self.sidebar_locators.SEARCH).clear()
        self.fill(self.sidebar_locators.SEARCH, text=search_value)  # Case validation / "AdMiN"
        self.check_search_results(self.sidebar_locators.ADMIN)
        self.driver.find_element(*self.sidebar_locators.SEARCH).clear()
        # self.fill(self.sidebar_locators.SEARCH, text=search_value) # No results / "Test"
        # self.driver.find_element(*self.sidebar_locators.SEARCH).clear()
        # self.fill(self.sidebar_locators.SEARCH, text=search_value) # Multiple matches / "D"
        # self.check_search_results(self.sidebar_locators.ADMIN, self.sidebar_locators.DASHBOARD,
        #                           self.sidebar_locators.DIRECTORY)

    # def check_sidebar_toggle(self):
    #     self.click(self.sidebar_locators.SIDEBAR_TOGGLE)

    # def check_search_with_negative_cases(self):
    #     self.

    def check_that_page_opened(self):
        self.should_be_visible(self.sidebar_locators)

    def check_sidebar_menu(self):
        self.should_be_visible(self.sidebar_locators.BANNER)
        self.should_be_visible(self.sidebar_locators.SEARCH)
        self.should_be_visible(self.sidebar_locators.SIDEBAR_TOGGLE)
        self.should_be_visible(self.sidebar_locators.ADMIN)
        self.should_be_visible(self.sidebar_locators.PIM)
        self.should_be_visible(self.sidebar_locators.LEAVE)
        self.should_be_visible(self.sidebar_locators.TIME)
        self.should_be_visible(self.sidebar_locators.RECRUITMENT)
        self.should_be_visible(self.sidebar_locators.MY_INFO)
        self.should_be_visible(self.sidebar_locators.PERFORMANCE)
        self.should_be_visible(self.sidebar_locators.DASHBOARD)
        self.should_be_visible(self.sidebar_locators.DIRECTORY)
        self.should_be_visible(self.sidebar_locators.MAINTENANCE)
        self.should_be_visible(self.sidebar_locators.CLAIM)
        self.should_be_visible(self.sidebar_locators.BUZZ)
