class MainPageLocators:
    def __init__(self, page):
        self.page = page
        self.MAIN_PAGE_TITLE = page.locator(".page-title").first
