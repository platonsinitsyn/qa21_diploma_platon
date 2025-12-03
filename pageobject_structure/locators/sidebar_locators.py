from selenium.webdriver.common.by import By

from pageobject_structure.core.base_page import BasePage


class SidebarLocators(BasePage):
    BANNER = By.CSS_SELECTOR, ".oxd-brand-banner"
    SEARCH = By.CSS_SELECTOR, "input[placeholder='Search']"
    SIDEBAR_TOGGLE = By.CSS_SELECTOR, "button.oxd-icon-button.oxd-main-menu-button"
    ADMIN = (By.CSS_SELECTOR, "aside a[href*='viewAdminModule']")
    PIM = (By.CSS_SELECTOR, "aside a[href*='viewPimModule']")
    LEAVE = (By.CSS_SELECTOR, "aside a[href*='viewLeaveModule']")
    TIME = (By.CSS_SELECTOR, "aside a[href*='viewTimeModule']")
    RECRUITMENT = (By.CSS_SELECTOR, "aside a[href*='viewRecruitmentModule']")
    MY_INFO = (By.CSS_SELECTOR, "aside a[href*='viewMyDetails']")
    PERFORMANCE = (By.CSS_SELECTOR, "aside a[href*='viewPerformanceModule']")
    DASHBOARD = (By.CSS_SELECTOR, "aside a[href*='dashboard']")
    DIRECTORY = (By.CSS_SELECTOR, "aside a[href*='viewDirectory']")
    MAINTENANCE = (By.CSS_SELECTOR, "aside a[href*='viewMaintenanceModule']")
    CLAIM = (By.CSS_SELECTOR, "aside a[href*='viewClaimModule']")
    BUZZ = (By.CSS_SELECTOR, "aside a[href*='viewBuzz']")
