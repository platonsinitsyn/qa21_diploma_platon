class AdminLocators:
    def __init__(self, page):
        self.page = page
        self.ADMIN_TITLE = page.locator(".oxd-table-filter-header")
