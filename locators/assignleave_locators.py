class AssignLeaveLocators:
    def __init__(self, page):
        self.page = page
        self.ASSIGN_LEAVE_TITLE = page.locator(".orangehrm-main-title")
