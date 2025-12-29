from playwright.sync_api import expect

from core.base_page import BasePage
from core.urls import URLS
from locators.login_locators import LoginLocators


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_locators = LoginLocators(page)

    def open_page(self):
        self.open(URLS.BASE + URLS.LOGIN)

    def login(self, username, password):
        self.login_locators.INPUT_USERNAME.fill(username)
        self.login_locators.INPUT_PASSWORD.fill(password)
        self.login_locators.SUBMIT.click()

    def check_that_page_opened(self, title, credits, os_number, license_text):
        expect(self.login_locators.LOGO).to_be_visible()
        expect(self.login_locators.SIDE_LOGO).to_be_visible()
        expect(self.login_locators.PAGE_TITLE).to_have_text(title)
        expect(self.login_locators.LOGIN_CREDS).to_have_text(credits)
        expect(self.login_locators.INPUT_USERNAME).to_be_visible()
        expect(self.login_locators.INPUT_PASSWORD).to_be_visible()
        expect(self.login_locators.SUBMIT).to_be_visible()
        expect(self.login_locators.FORGOT_BUTTON).to_be_visible()
        expect(self.login_locators.FOOTER_OS).to_have_text(os_number)
        expect(self.login_locators.FOOTER_LICENSE).to_have_text(license_text)
        expect(self.login_locators.FOOTER_LINK).to_be_visible()
        expect(self.login_locators.LINKEDIN_LINK).to_be_visible()
        expect(self.login_locators.FACEBOOK_LINK).to_be_visible()
        expect(self.login_locators.TWITTER_LINK).to_be_visible()
        expect(self.login_locators.YOUTUBE_LINK).to_be_visible()
        expect(self.login_locators.ERROR).not_to_be_visible()

    def check_that_error_is_visible(self, text):
        expect(self.login_locators.ERROR).to_be_visible()
        expect(self.login_locators.ERROR).to_have_text(text)
