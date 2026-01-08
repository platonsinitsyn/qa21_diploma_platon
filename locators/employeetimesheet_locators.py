class EmployeeTimesheetsLocators:
    def __init__(self, page):
        self.page = page
        self.EMPLOYEE_TIMESHEETS_TITLE = page.locator(".orangehrm-main-title").first
        self.TIMESHEETS_PENDING_TITLE = page.locator(".orangehrm-main-title").last
