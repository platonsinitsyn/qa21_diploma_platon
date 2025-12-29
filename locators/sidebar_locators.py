class SidebarLocators:
    def __init__(self, page):
        self.page = page
        self.BANNER = page.locator(".oxd-brand-banner")
        self.SEARCH = page.locator("input[placeholder='Search']")
        self.SIDEBAR_TOGGLE = page.locator("button.oxd-icon-button.oxd-main-menu-button")
        self.ADMIN = page.locator("a[href*='viewAdminModule']")
        self.PIM = page.locator("a[href*='viewPimModule']")
        self.LEAVE = page.locator("a[href*='viewLeaveModule']")
        self.TIME = page.locator("a[href*='viewTimeModule']")
        self.RECRUITMENT = page.locator("a[href*='viewRecruitmentModule']")
        self.MY_INFO = page.locator("a[href*='viewMyDetails']")
        self.PERFORMANCE = page.locator("a[href*='viewPerformanceModule']")
        self.DASHBOARD = page.locator("a[href*='dashboard']")
        self.DIRECTORY = page.locator("a[href*='viewDirectory']")
        self.MAINTENANCE = page.locator("a[href*='viewMaintenanceModule']")
        self.CLAIM = page.locator("a[href*='viewClaimModule']")
        self.BUZZ = page.locator("a[href*='viewBuzz']")
