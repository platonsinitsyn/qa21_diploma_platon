class DashboardLocators:
    def __init__(page):
        self.page = page
        self.DASHBOARD_TITLE = page.locator(".oxd-topbar-header-breadcrumb")

        QUESTION_LINK = ".oxd-icon.bi-question-lg"
        TIME_AT_WORK_SECTION = ".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(1)"
        MY_ACTIONS_SECTION = ".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(2)"
        QUICK_LAUNCH_SECTION = ".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(3)"
        BUZZ_POSTS_SECTION = ".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(4)"
        LEAVE_TODAY_SECTION = ".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(5)"
        DISTRIBUTION_SECTION_SUBUNIT = ".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(6)"
        DISTRIBUTION_SECTION_LOCATION = ".oxd-grid-item.oxd-grid-item--gutters:nth-of-type(7)"
        ASSIGN_LEAVE_BTN = "button[title='Assign Leave']"
        LEAVE_LIST_BTN = "button[title='Leave List']"
        TIMESHEETS_BTN = "button[title='Timesheets']"
        APPLY_LEAVE_BTN = "button[title='Apply Leave']"
        MY_LEAVE_BTN = "button[title='My Leave']"
        MY_TIMESHEET_BTN = "button[title='My Timesheet']"

    def get_buttons(title):
        return page.locator(f"button[title='{title}']")
