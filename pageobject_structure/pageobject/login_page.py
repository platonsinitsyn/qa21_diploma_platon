from selenium.webdriver.common.by import By

from pageobject_structure.core.base_page import BasePage
from pageobject_structure.urls import URLS


class LoginPage(BasePage):
    LOGO = By.CSS_SELECTOR, ".orangehrm-login-branding"
    SIDE_LOGO = By.XPATH, "//*[@id='app']/div[1]/div/div[2]"
    PAGE_TITLE = By.CSS_SELECTOR, ".oxd-text.oxd-text--h5.orangehrm-login-title"
    LOGIN_CREDS = By.CSS_SELECTOR, ".orangehrm-login-error"
    INPUT_USERNAME = By.CSS_SELECTOR, "input[placeholder='Username']"
    INPUT_PASSWORD = By.CSS_SELECTOR, "input[placeholder='Password']"
    SUBMIT = By.CSS_SELECTOR, "button[type='submit']"
    FORGOT_BUTTON = By.CSS_SELECTOR, ".orangehrm-login-forgot-header"
    FOOTER_OS = By.CSS_SELECTOR, ".orangehrm-copyright-wrapper p:first-of-type"
    FOOTER_LICENSE = By.CSS_SELECTOR, ".orangehrm-copyright-wrapper p:last-of-type"
    FOOTER_LINK = By.CSS_SELECTOR, ".orangehrm-copyright-wrapper a"
    LINKEDIN_LINK = By.CSS_SELECTOR, "a[href*='linkedin.com']"
    FACEBOOK_LINK = By.CSS_SELECTOR, "a[href*='facebook.com']"
    TWITTER_LINK = By.CSS_SELECTOR, "a[href*='twitter.com']"
    YOUTUBE_LINK = By.CSS_SELECTOR, "a[href*='youtube.com']"
    ERROR = By.CSS_SELECTOR, ".oxd-alert.oxd-alert--error"

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.open(URLS.BASE + URLS.LOGIN)

    def check_that_page_opened(self, title, credits, os_number, license_text):
        self.should_be_visible(self.LOGO)
        self.should_be_visible(self.SIDE_LOGO)
        self.should_be_has_text(self.PAGE_TITLE, title)
        self.should_be_has_text(self.LOGIN_CREDS, credits)
        self.should_be_visible(self.INPUT_USERNAME)
        self.should_be_visible(self.INPUT_PASSWORD)
        self.should_be_visible(self.SUBMIT)
        self.should_be_visible(self.FORGOT_BUTTON)
        self.should_be_has_text(self.FOOTER_OS, os_number)
        self.should_be_has_text(self.FOOTER_LICENSE, license_text)
        self.should_be_visible(self.FOOTER_LINK)
        self.should_be_visible(self.LINKEDIN_LINK)
        self.should_be_visible(self.FACEBOOK_LINK)
        self.should_be_visible(self.TWITTER_LINK)
        self.should_be_visible(self.YOUTUBE_LINK)
        self.should_be_not_visible(self.ERROR)

    def login(self, username, password):
        self.fill(self.INPUT_USERNAME, text=username)
        self.fill(self.INPUT_PASSWORD, text=password)
        self.click(self.SUBMIT)

    def check_that_error_is_visible(self, text):
        self.should_be_visible(self.ERROR)
        self.should_be_has_text(self.ERROR, text)
