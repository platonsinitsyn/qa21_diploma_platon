class PimLocators:
    def __init__(self, page):
        self.page = page
        # PIM MAIN PAGE:
        self.PIM_TITLE = page.locator(".oxd-table-filter-header")
        self.TOP_TAB_CONFIGURATION = page.locator(".oxd-topbar-body-nav-tab-item").nth(0)
        self.TOP_TAB_EMPLOYEE_LIST = page.locator(".oxd-topbar-body-nav-tab-item").nth(1)
        self.TOP_TAB_ADD_EMPLOYEE = page.locator(".oxd-topbar-body-nav-tab-item").nth(2)
        self.TOP_TAB_REPORTS = page.locator(".oxd-topbar-body-nav-tab-item").nth(3)
        self.QUESTION_LINK = page.locator(".oxd-icon.bi-question-lg")
        self.ADD_BUTTON = page.get_by_role("button", name=" Add ")
        self.RESET_BUTTON = page.get_by_role("button", name=" Reset ")
        self.SEARCH_BUTTON = page.get_by_role("button", name=" Search ")
        self.RECORDS_COUNT = page.locator(".oxd-text--span:has-text('Records Found')")
        self.EMPLOYEE_NAME_LABEL = page.locator("label.oxd-label", has_text="Employee Name")
        self.EMPLOYEE_ID_LABEL = page.locator("label.oxd-label", has_text="Employee Id")
        self.EMPLOYMENT_STATUS_LABEL = page.locator("label.oxd-label", has_text="Employment Status")
        self.INCLUDE_LABEL = page.locator("label.oxd-label", has_text="Include")
        self.SUPERVISOR_NAME_LABEL = page.locator("label.oxd-label", has_text="Supervisor Name")
        self.JOB_TITLE_LABEL = page.locator("label.oxd-label", has_text="Job Title")
        self.SUB_UNIT_LABEL = page.locator("label.oxd-label", has_text="Sub Unit")
        self.EMPLOYEE_NAME_INPUT = page.locator(".oxd-autocomplete-wrapper").first.locator("input")
        self.EMPLOYEE_ID_INPUT = page.locator(".oxd-input-group:has(label.oxd-label:has-text('Employee Id')) input")
        self.EMPLOYMENT_STATUS_DROPDOWN = page.locator(
            ".oxd-input-group:has(label.oxd-label:has-text('Employment Status')) .oxd-select-text"
        )
        self.INCLUDE_DROPDOWN = page.locator(
            ".oxd-input-group:has(label.oxd-label:has-text('Include')) .oxd-select-text"
        )
        self.SUPERVISOR_NAME_INPUT = page.locator(".oxd-autocomplete-wrapper").last.locator("input")
        self.JOB_TITLE_DROPDOWN = page.locator(
            ".oxd-input-group:has(label.oxd-label:has-text('Job Title')) .oxd-select-text"
        )
        self.SUB_UNIT_DROPDOWN = page.locator(
            ".oxd-input-group:has(label.oxd-label:has-text('Sub Unit')) .oxd-select-text"
        )
        # ADD EMPLOYEE BUTTON:
        self.ADD_EMPLOYEE_TITLE = page.locator(".orangehrm-main-title")
        self.EMPLOYEE_FULL_NAME_TITLE = page.locator(".oxd-label").first
        self.FIRST_NAME_FIELD = page.locator(".orangehrm-firstname")
        self.MIDDLE_NAME_FIELD = page.locator(".orangehrm-middlename")
        self.LAST_NAME_FIELD = page.locator(".orangehrm-lastname")
        self.EMPLOYEE_ID_TITLE = page.locator(".oxd-label").last
        self.EMPLOYEE_ID_FIELD = page.locator(".oxd-input--active").last
        self.REQUIRED_TEXT = page.locator(".orangehrm-form-hint:has-text('Required')")
        self.ADD_PHOTO_BUTTON = page.locator(".employee-image-action")
        self.PHOTO_HINT_TEXT = page.locator(".orangehrm-input-hint")
        self.CREATE_LOGIN_TEXT = page.locator(".user-form-header-text")
        self.LOGIN_DETAILS_RADIOBUTTON = page.locator(".oxd-switch-wrapper")
        self.CANCEL_BUTTON = page.locator(".oxd-button--ghost")
        self.SAVE_BUTTON = page.locator(".orangehrm-left-space")
        # PERSONAL DETAILS PAGE:
        self.PERSONAL_DETAILS_PAGE = page.locator(".orangehrm-edit-employee-name")
        self.PD_FIRST_NAME = page.locator(".orangehrm-firstname")
        self.PD_MIDDLE_NAME = page.locator(".orangehrm-middlename")
        self.PD_LAST_NAME = page.locator(".orangehrm-lastname")
