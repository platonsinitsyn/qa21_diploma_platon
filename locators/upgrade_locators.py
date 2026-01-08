class UpgradeLocators:
    def __init__(self, page):
        self.page = page
        self.FOOTER_TITLE = page.locator("#footer-btn h1")
