from selenium.webdriver.common.by import By

from pageobject_structure.core.base_page import BasePage


class DashboardPage(BasePage):
    DASHBOARD_TITLE = By.XPATH, "//h6[text()='Dashboard']"
    UPGRADE_BUTTON = By.CSS_SELECTOR, ".oxd-glass-button.orangehrm-upgrade-button"
    USER_DROPDOWN = By.CSS_SELECTOR, ".oxd-userdropdown-tab"
    ABOUT_BUTTON = By.XPATH, "//a[text()='About']"
    SUPPORT_BUTTON = By.XPATH, "//a[text()='Support']"
    CHANGE_PASSWORD_BUTTON = By.XPATH, "//a[text()='Change Password']"
    LOGOUT_BUTTON = By.XPATH, "//a[text()='Logout']"
    QUESTION_LINK = By.CSS_SELECTOR, ".oxd-icon.bi-question-lg"

    def __init__(self, driver):
        super().__init__(driver)

    def check_that_page_opened(self, title):
        self.should_be_has_text(self.DASHBOARD_TITLE, title)
        self.should_be_visible(self.UPGRADE_BUTTON)
        self.should_be_visible(self.USER_DROPDOWN)

    #       self.should_be_visible(self.x)

    def click_logout(self):
        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT_BUTTON)
