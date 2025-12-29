class HeaderLocators:
    def __init__(self, page):
        self.page = page
        self.UPGRADE_BUTTON = page.locator(".orangehrm-upgrade-container")
        self.USER_DROPDOWN = page.locator(".oxd-userdropdown")
        self.ABOUT_BUTTON = page.locator("ul.oxd-dropdown-menu li:nth-child(1) a.oxd-userdropdown-link")
        self.SUPPORT_BUTTON = page.locator("ul.oxd-dropdown-menu li:nth-child(2) a.oxd-userdropdown-link")
        self.CHANGE_PASSWORD_BUTTON = page.locator("ul.oxd-dropdown-menu li:nth-child(3) a.oxd-userdropdown-link")
        self.LOGOUT_BUTTON = page.locator("ul.oxd-dropdown-menu li:nth-child(4) a.oxd-userdropdown-link")
        self.ABOUT_MODAL = page.locator(".oxd-dropdown-menu")
        self.ABOUT_HEADER = page.locator(
            "//div[contains(@class,'oxd-dialog-container')]//h6[contains(@class,'orangehrm-main-title')]"
        )
        self.ABOUT_CLOSE_BTN = page.locator(".oxd-dialog-close-button")
        self.COMPANY_NAME_LABEL = page.locator("//p[normalize-space()='Company Name:']")
        self.COMPANY_NAME_TEXT = page.locator("//*[@id='app']/div[2]/div/div/div/div[2]/div[2]/p")
        self.VERSION_LABEL = page.locator("//p[normalize-space()='Version:']")
        self.VERSION_TEXT = page.locator("//*[@id='app']/div[2]/div/div/div/div[2]/div[4]/p")
        self.EMPLOYEES_LABEL = page.locator("//p[normalize-space()='Active Employees:']")
        self.EMPLOYEES_TEXT = page.locator("//*[@id='app']/div[2]/div/div/div/div[2]/div[6]/p")
        self.TERMINATED_LABEL = page.locator("//p[normalize-space()='Employees Terminated:']")
        self.TERMINATED_TEXT = page.locator("//*[@id='app']/div[2]/div/div/div/div[2]/div[8]/p")
