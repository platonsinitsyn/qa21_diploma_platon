class LoginLocators:
    def __init__(self, page):
        self.page = page
        self.LOGO = page.locator(".orangehrm-login-branding")
        self.SIDE_LOGO = page.locator("//*[@id='app']/div[1]/div/div[2]")
        self.PAGE_TITLE = page.locator(".oxd-text.oxd-text--h5.orangehrm-login-title")
        self.LOGIN_CREDS = page.locator(".orangehrm-login-error")
        self.INPUT_USERNAME = page.locator("[name='username']")
        self.INPUT_PASSWORD = page.locator("[name='password']")
        self.SUBMIT = page.locator("button[type='submit']")
        self.FORGOT_BUTTON = page.locator(".orangehrm-login-forgot-header")
        self.FOOTER_OS = page.locator(".orangehrm-copyright-wrapper p:first-of-type")
        self.FOOTER_LICENSE = page.locator(".orangehrm-copyright-wrapper p:last-of-type")
        self.FOOTER_LINK = page.locator(".orangehrm-copyright-wrapper a")
        self.LINKEDIN_LINK = page.locator("a[href*='linkedin.com']")
        self.FACEBOOK_LINK = page.locator("a[href*='facebook.com']")
        self.TWITTER_LINK = page.locator("a[href*='twitter.com']")
        self.YOUTUBE_LINK = page.locator("a[href*='youtube.com']")
        self.ERROR = page.locator(".oxd-alert.oxd-alert--error")
