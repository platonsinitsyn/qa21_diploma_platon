class BuzzLocators:
    def __init__(self, page):
        self.page = page
        self.BUZZ_TITLE = page.locator(".orangehrm-buzz-newsfeed-title")
