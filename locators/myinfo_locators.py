class MyInfoLocators:
    def __init__(self, page):
        self.page = page
        self.PERSONAL_DETAILS_TAB = page.locator(".orangehrm-main-title").first
