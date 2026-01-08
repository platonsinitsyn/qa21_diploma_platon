class MyTimesheetLocators:
    def __init__(self, page):
        self.page = page
        self.MY_TIMESHEET_TITLE = page.locator(".orangehrm-main-title")
