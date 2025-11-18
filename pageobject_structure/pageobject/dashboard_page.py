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
    TIME_AT_WORK_SECTION = By.CSS_SELECTOR, ".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(1)"
    MY_ACTIONS_SECTION = By.CSS_SELECTOR, ".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(2)"
    QUICK_LAUNCH_SECTION = By.CSS_SELECTOR, ".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(3)"
    BUZZ_POSTS_SECTION = By.CSS_SELECTOR, ".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(4)"
    LEAVE_TODAY_SECTION = By.CSS_SELECTOR, ".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(5)"
    DISTRIBUTION_SECTION_SUBUNIT = By.CSS_SELECTOR, ".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(6)"
    DISTRIBUTION_SECTION_LOCATION = By.CSS_SELECTOR, ".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(7)"
    ASSIGN_LEAVE_BTN = By.CSS_SELECTOR, "button[title='Assign Leave']"
    LEAVE_LIST_BTN = By.CSS_SELECTOR, "button[title='Leave List']"
    TIMESHEETS_BTN = By.CSS_SELECTOR, "button[title='Timesheets']"
    APPLY_LEAVE_BTN = By.CSS_SELECTOR, "button[title='Apply Leave']"
    MY_LEAVE_BTN = By.CSS_SELECTOR, "button[title='My Leave']"
    MY_TIMESHEET_BTN = By.CSS_SELECTOR, "button[title='My Timesheet']"

    def __init__(self, driver):
        super().__init__(driver)

    def click_logout(self):
        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT_BUTTON)

    def check_quick_assign(self):
        self.click(self.ASSIGN_LEAVE_BTN)

    def check_quick_leave(self):
        self.click(self.LEAVE_LIST_BTN)

    def check_quick_timesheets(self):
        self.click(self.TIMESHEETS_BTN)

    def check_quick_apply(self):
        self.click(self.APPLY_LEAVE_BTN)

    def check_quick_my_leave(self):
        self.click(self.MY_LEAVE_BTN)

    def check_quick_my_timesheet(self):
        self.click(self.MY_TIMESHEET_BTN)

    def check_that_page_opened(self, title):
        self.should_be_has_text(self.DASHBOARD_TITLE, title)
        self.should_be_visible(self.UPGRADE_BUTTON)
        self.should_be_visible(self.USER_DROPDOWN)

    def check_that_all_sections_displayed(self):
        self.should_be_visible(self.TIME_AT_WORK_SECTION)
        self.should_be_visible(self.MY_ACTIONS_SECTION)
        self.should_be_visible(self.QUICK_LAUNCH_SECTION)
        self.should_be_visible(self.BUZZ_POSTS_SECTION)
        self.should_be_visible(self.LEAVE_TODAY_SECTION)
        self.should_be_visible(self.DISTRIBUTION_SECTION_SUBUNIT)
        self.should_be_visible(self.DISTRIBUTION_SECTION_LOCATION)
