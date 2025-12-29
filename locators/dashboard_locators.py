class DashboardLocators:
    def __init__(self, page):
        self.page = page
        self.DASHBOARD_TITLE = page.locator(".oxd-topbar-header-breadcrumb")
        self.QUESTION_LINK = page.locator(".oxd-icon.bi-question-lg")
        self.TIME_AT_WORK_SECTION = page.locator(".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(1)")
        self.MY_ACTIONS_SECTION = page.locator(".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(2)")
        self.QUICK_LAUNCH_SECTION = page.locator(".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(3)")
        self.BUZZ_POSTS_SECTION = page.locator(".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(4)")
        self.LEAVE_TODAY_SECTION = page.locator(".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(5)")
        self.DISTRIBUTION_SECTION_SUBUNIT = page.locator(".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(6)")
        self.DISTRIBUTION_SECTION_LOCATION = page.locator(".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(7)")
        self.ASSIGN_LEAVE_BTN = page.locator("button[title='Assign Leave']")
        self.LEAVE_LIST_BTN = page.locator("button[title='Leave List']")
        self.TIMESHEETS_BTN = page.locator("button[title='Timesheets']")
        self.APPLY_LEAVE_BTN = page.locator("button[title='Apply Leave']")
        self.MY_LEAVE_BTN = page.locator("button[title='My Leave']")
        self.MY_TIMESHEET_BTN = page.locator("button[title='My Timesheet']")

    def get_buttons(self, title):
        return self.page.locator(f"button[title='{title}']")
