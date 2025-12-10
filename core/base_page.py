from playwright.sync_api import expect


class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def click(self, selector):
        self.page.locator(selector).click()

    def fill(self, selector, text: str):
        self.page.locator(selector).fill(text)

    def page_should_be_opened(self, expected_url, title=None):
        expect(self.page).to_have_url(expected_url)
        if title:
            expect(self.page).to_have_title(title)

    def should_has_text(self, selector, expected):
        expect(self.page.locator(selector)).to_have_text(expected)

    def should_be_visible(self, selector, is_visible=True):
        if is_visible:
            expect(self.page.locator(selector)).to_be_visible()
        else:
            self.should_be_not_visible(selector)

    def should_be_not_visible(self, selector):
        expect(self.page.locator(selector)).not_to_be_visible()
