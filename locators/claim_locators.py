class ClaimLocators:
    def __init__(self, page):
        self.page = page
        self.EMPLOYEE_CLAIMS_TITLE = page.locator(".oxd-table-filter-title")
