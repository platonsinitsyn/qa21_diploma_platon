class ApplyLeaveLocators:
    def __init__(self, page):
        self.page = page
        self.APPLY_LEAVE_TITLE = page.locator(".orangehrm-main-title")
