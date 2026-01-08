class RecruitmentLocators:
    def __init__(self, page):
        self.page = page
        self.RECRUITMENT_TITLE = page.locator(".oxd-topbar-header-breadcrumb-module")
