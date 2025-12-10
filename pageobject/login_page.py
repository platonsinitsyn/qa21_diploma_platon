from core.base_page import BasePage
from core.urls import URLS
from pageobject.locators.login_locators import LoginLocators


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_locators = LoginLocators

    def open_page(self):
        self.open(URLS.BASE + URLS.LOGIN)

    def login(self, username, password):
        self.fill(self.login_locators.INPUT_USERNAME, text=username)
        self.fill(self.login_locators.INPUT_PASSWORD, text=password)
        self.click(self.login_locators.SUBMIT)

    def check_that_page_opened(self, title, credits, os_number, license_text):
        self.should_be_visible(self.login_locators.LOGO)
        self.should_be_visible(self.login_locators.SIDE_LOGO)
        self.should_has_text(self.login_locators.PAGE_TITLE, title)
        self.should_has_text(self.login_locators.LOGIN_CREDS, credits)
        self.should_be_visible(self.login_locators.INPUT_USERNAME)
        self.should_be_visible(self.login_locators.INPUT_PASSWORD)
        self.should_be_visible(self.login_locators.SUBMIT)
        self.should_be_visible(self.login_locators.FORGOT_BUTTON)
        self.should_has_text(self.login_locators.FOOTER_OS, os_number)
        self.should_has_text(self.login_locators.FOOTER_LICENSE, license_text)
        self.should_be_visible(self.login_locators.FOOTER_LINK)
        self.should_be_visible(self.login_locators.LINKEDIN_LINK)
        self.should_be_visible(self.login_locators.FACEBOOK_LINK)
        self.should_be_visible(self.login_locators.TWITTER_LINK)
        self.should_be_visible(self.login_locators.YOUTUBE_LINK)
        self.should_be_not_visible(self.login_locators.ERROR)

    def check_that_error_is_visible(self, text):
        self.should_be_visible(self.login_locators.ERROR)
        self.should_has_text(self.login_locators.ERROR, text)
