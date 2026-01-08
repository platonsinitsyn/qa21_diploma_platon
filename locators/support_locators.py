class SupportLocators:
    def __init__(self, page):
        self.page = page
        self.SUPPORT_TITLE = page.locator(".orangehrm-sub-title")
