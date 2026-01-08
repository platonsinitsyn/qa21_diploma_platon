from playwright.sync_api import expect
from core.base_page import BasePage
from locators.dashboard_locators import DashboardLocators
from locators.header_locators import HeaderLocators
from locators.upgrade_locators import UpgradeLocators
from locators.support_locators import SupportLocators
from locators.login_locators import LoginLocators


class HeaderObject(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.header_locators = HeaderLocators(page)
        self.dashboard_locators = DashboardLocators(page)
        self.upgrade_locators = UpgradeLocators(page)
        self.support_locators = SupportLocators(page)
        self.login_locators = LoginLocators(page)

    def click_upgrade(self):
        self.header_locators.UPGRADE_BUTTON.click()

    def click_support(self):
        self.header_locators.USER_DROPDOWN.click()
        self.header_locators.SUPPORT_BUTTON.click()

    def click_change_password(self):
        self.header_locators.USER_DROPDOWN.click()
        self.header_locators.CHANGE_PASSWORD_BUTTON.click()

    def click_logout(self):
        self.header_locators.USER_DROPDOWN.click()
        self.header_locators.LOGOUT_BUTTON.click()

    def switch_to_new_tab(self, expected_tabs=2, timeout=10):
        self.page.context.wait_for_event("page", timeout=timeout * 1000)
        new_page = self.page.context.pages[-1]
        self.page = new_page
        self.upgrade_locators = UpgradeLocators(self.page)
        self.header_locators = HeaderLocators(self.page)
        self.dashboard_locators = DashboardLocators(self.page)

    def page_should_be_opened(self, expected_url, title=None):
        expect(self.page).to_have_url(expected_url)
        if title:
            expect(self.page).to_have_title(title)

    def open_modal(self):
        self.header_locators.USER_DROPDOWN.click()
        self.header_locators.ABOUT_BUTTON.click()

    def close_modal(self):
        self.header_locators.ABOUT_CLOSE_BTN.click()

    def check_modal_is_opened(self):
        expect(self.header_locators.ABOUT_HEADER).to_be_visible()
        expect(self.header_locators.COMPANY_NAME_LABEL).to_be_visible()
        expect(self.header_locators.COMPANY_NAME_TEXT).to_be_visible()
        expect(self.header_locators.VERSION_LABEL).to_be_visible()
        expect(self.header_locators.VERSION_TEXT).to_be_visible()
        expect(self.header_locators.EMPLOYEES_LABEL).to_be_visible()
        expect(self.header_locators.EMPLOYEES_TEXT).to_be_visible()
        expect(self.header_locators.TERMINATED_LABEL).to_be_visible()
        expect(self.header_locators.TERMINATED_TEXT).to_be_visible()
        expect(self.header_locators.ABOUT_CLOSE_BTN).to_be_visible()

    def check_upgrade_is_opened(self):
        expect(self.upgrade_locators.FOOTER_TITLE).to_be_visible()
        expect(self.upgrade_locators.FOOTER_TITLE).to_have_text(
            "Unlock the full potential of your HR with OrangeHRM Advanced."
        )

    def check_support_is_opened(self):
        expect(self.support_locators.SUPPORT_TITLE).to_be_visible()

    def check_modal_is_closed(self):
        expect(self.header_locators.ABOUT_HEADER).not_to_be_visible()
