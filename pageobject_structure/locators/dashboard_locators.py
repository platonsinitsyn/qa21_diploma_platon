from selenium.webdriver.common.by import By

from pageobject_structure.core.base_page import BasePage


class DashboardLocators(BasePage):
    DASHBOARD_TITLE = By.XPATH, "//h6[text()='Dashboard']"
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
