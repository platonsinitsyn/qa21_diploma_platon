from selenium.webdriver.common.by import By

from pageobject_structure.core.base_page import BasePage


class LoginLocators(BasePage):
    LOGO = By.CSS_SELECTOR, ".orangehrm-login-branding"
    SIDE_LOGO = By.XPATH, "//*[@id='app']/div[1]/div/div[2]"
    PAGE_TITLE = By.CSS_SELECTOR, ".oxd-text.oxd-text--h5.orangehrm-login-title"
    LOGIN_CREDS = By.CSS_SELECTOR, ".orangehrm-login-error"
    INPUT_USERNAME = By.NAME, "username"
    INPUT_PASSWORD = By.NAME, "password"
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
