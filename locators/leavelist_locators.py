class ViewLeaveListLocators:
    def __init__(self, page):
        self.page = page
        self.LEAVE_LIST_TITLE = page.locator(".oxd-table-filter-header")
