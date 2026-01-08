class DirectoryLocators:
    def __init__(self, page):
        self.page = page
        self.DIRECTORY_TITLE = page.locator(".oxd-table-filter-title")
