from selenium.webdriver.support import expected_conditions as EC

from pageobject_structure.core.base_page import BasePage
from pageobject_structure.locators.dashboard_locators import DashboardLocators
from pageobject_structure.locators.header_locators import HeaderLocators


class HeaderObject(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.header_locators = HeaderLocators(driver)
        self.dashboard_locators = DashboardLocators(driver)

    def click_upgrade(self):
        self.click(self.header_locators.UPGRADE_BUTTON)

    def click_support(self):
        self.click(self.header_locators.USER_DROPDOWN)
        self.click(self.header_locators.SUPPORT_BUTTON)

    def click_change_password(self):
        self.click(self.header_locators.USER_DROPDOWN)
        self.click(self.header_locators.CHANGE_PASSWORD_BUTTON)

    def click_logout(self):
        self.click(self.header_locators.USER_DROPDOWN)
        self.click(self.header_locators.LOGOUT_BUTTON)

    def switch_to_new_tab(self, expected_tabs=2, timeout=10):
        self.wait.until(EC.number_of_windows_to_be(expected_tabs))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def check_about_modal(self):
        self.click(self.header_locators.USER_DROPDOWN)
        self.click(self.header_locators.ABOUT_BUTTON)
        self.should_be_visible(self.header_locators.ABOUT_HEADER)
        self.should_be_visible(self.header_locators.COMPANY_NAME_LABEL)
        self.should_be_visible(self.header_locators.COMPANY_NAME_TEXT)
        self.should_be_visible(self.header_locators.VERSION_LABEL)
        self.should_be_visible(self.header_locators.VERSION_TEXT)
        self.should_be_visible(self.header_locators.EMPLOYEES_LABEL)
        self.should_be_visible(self.header_locators.EMPLOYEES_TEXT)
        self.should_be_visible(self.header_locators.TERMINATED_LABEL)
        self.should_be_visible(self.header_locators.TERMINATED_TEXT)
        self.should_be_visible(self.header_locators.ABOUT_CLOSE_BTN)
        self.click(self.header_locators.ABOUT_CLOSE_BTN)
        self.should_be_not_visible(self.header_locators.ABOUT_HEADER)
