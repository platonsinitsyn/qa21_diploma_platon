class PerformanceLocators:
    def __init__(self, page):
        self.page = page
        self.PERFORMANCE_TITLE = page.locator(".oxd-topbar-header-breadcrumb-module")
