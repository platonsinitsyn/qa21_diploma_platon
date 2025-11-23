from playwright.sync_api import expect

from pageobject_structure.core.base_page import BasePage
from pageobject_structure.locators.dashboard_locators import DashboardLocators
from pageobject_structure.locators.header_locators import HeaderLocators


class HeaderObject(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.header_locators = HeaderLocators
        self.dashboard_locators = DashboardLocators

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
        self.page.context.wait_for_event("page", timeout=timeout * 1000)
        pages = self.page.context.pages
        new_page = pages[-1]
        self.page = new_page

    def page_should_be_opened(self, expected_url, title=None):
        expect(self.page).to_have_url(expected_url)
        if title:
            expect(self.page).to_have_title(title)

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
