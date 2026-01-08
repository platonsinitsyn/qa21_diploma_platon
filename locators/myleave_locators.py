class MyLeaveLocators:
    def __init__(self, page):
        self.page = page
        self.MY_LEAVE_LIST_TITLE = page.locator(".oxd-table-filter-title")
