from selenium.webdriver.common.by import By

from pageobject_structure.core.base_page import BasePage


class HeaderLocators(BasePage):
    UPGRADE_BUTTON = By.CSS_SELECTOR, ".oxd-glass-button.orangehrm-upgrade-button"
    USER_DROPDOWN = By.CSS_SELECTOR, ".oxd-userdropdown-tab"
    ABOUT_BUTTON = By.XPATH, "//a[text()='About']"
    SUPPORT_BUTTON = By.XPATH, "//a[text()='Support']"
    CHANGE_PASSWORD_BUTTON = By.XPATH, "//a[text()='Change Password']"
    LOGOUT_BUTTON = By.XPATH, "//a[text()='Logout']"
    # ABOUT MODAL
    ABOUT_MODAL = (By.CSS_SELECTOR, ".oxd-dialog-container")
    ABOUT_HEADER = (By.XPATH, "//h6[normalize-space()='About']")
    ABOUT_CLOSE_BTN = (By.CSS_SELECTOR, ".oxd-dialog-close-button")
    COMPANY_NAME_LABEL = (By.XPATH, "//p[normalize-space()='Company Name:']")
    COMPANY_NAME_TEXT = (By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[2]/div[2]/p")
    VERSION_LABEL = (By.XPATH, "//p[normalize-space()='Version:']")
    VERSION_TEXT = (By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[2]/div[4]/p")
    EMPLOYEES_LABEL = (By.XPATH, "//p[normalize-space()='Active Employees:']")
    EMPLOYEES_TEXT = (By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[2]/div[6]/p")
    TERMINATED_LABEL = (By.XPATH, "//p[normalize-space()='Employees Terminated:']")
    TERMINATED_TEXT = (By.XPATH, "//*[@id='app']/div[2]/div/div/div/div[2]/div[8]/p")
