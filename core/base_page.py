from playwright.sync_api import expect


class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def page_should_be_opened(self, expected_url, title=None):
        expect(self.page).to_have_url(expected_url)
        if title:
            expect(self.page).to_have_title(title)
