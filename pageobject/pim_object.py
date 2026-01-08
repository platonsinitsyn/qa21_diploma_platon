from playwright.sync_api import expect

from core.base_page import BasePage
from locators.pim_locators import PimLocators
from locators.sidebar_locators import SidebarLocators


class PimPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.pim_locators = PimLocators(page)
        self.sidebar_locators = SidebarLocators(page)

    def click_pim_tab(self):
        self.sidebar_locators.PIM.click()

    def click_add_employee_tab(self):
        self.pim_locators.TOP_TAB_ADD_EMPLOYEE.click()

    def click_save_button(self):
        self.pim_locators.SAVE_BUTTON.click()

    def click_cancel_button(self):
        self.pim_locators.CANCEL_BUTTON.click()

    def click_search_button(self):
        self.pim_locators.SEARCH_BUTTON.click()

    def fill_and_check_input(self, field, value: str):
        field.fill(value)
        expect(field).to_have_value(value)

    def select_and_check_dropdown(self, dropdown, option_text: str):
        dropdown.click()
        self.page.get_by_role("option", name=option_text).click()
        expect(dropdown).to_contain_text(option_text)

    def row_with_text_should_be_visible(self, value: str):
        row = self.page.locator(".oxd-table-row").filter(has_text=value)
        expect(row).to_be_visible()

    def enter_employee_data(self, first_name, middle_name, last_name):
        self.pim_locators.FIRST_NAME_FIELD.fill(first_name)
        self.pim_locators.MIDDLE_NAME_FIELD.fill(middle_name)
        self.pim_locators.LAST_NAME_FIELD.fill(last_name)

    def check_new_employee_is_created(self):
        expect(self.pim_locators.TOP_TAB_ADD_EMPLOYEE).to_be_visible()
        expect(self.pim_locators.PERSONAL_DETAILS_PAGE).to_be_visible(timeout=15000)
        expect(self.pim_locators.PD_FIRST_NAME).not_to_have_value("")
        expect(self.pim_locators.PD_MIDDLE_NAME).not_to_have_value("")
        expect(self.pim_locators.PD_LAST_NAME).not_to_have_value("")

    def check_employee_list_page(self):
        expect(self.pim_locators.PIM_TITLE).to_be_visible()
        expect(self.pim_locators.TOP_TAB_CONFIGURATION).to_be_visible()
        expect(self.pim_locators.TOP_TAB_EMPLOYEE_LIST).to_be_visible()
        expect(self.pim_locators.TOP_TAB_ADD_EMPLOYEE).to_be_visible()
        expect(self.pim_locators.TOP_TAB_REPORTS).to_be_visible()
        expect(self.pim_locators.ADD_BUTTON).to_be_visible()
        expect(self.pim_locators.EMPLOYEE_NAME_LABEL).to_be_visible()
        expect(self.pim_locators.EMPLOYEE_NAME_INPUT).to_be_visible()
        expect(self.pim_locators.EMPLOYEE_ID_LABEL).to_be_visible()
        expect(self.pim_locators.EMPLOYEE_ID_INPUT).to_be_visible()
        expect(self.pim_locators.EMPLOYMENT_STATUS_LABEL).to_be_visible()
        expect(self.pim_locators.EMPLOYMENT_STATUS_DROPDOWN).to_be_visible()
        expect(self.pim_locators.INCLUDE_LABEL).to_be_visible()
        expect(self.pim_locators.INCLUDE_DROPDOWN).to_be_visible()
        expect(self.pim_locators.SUPERVISOR_NAME_LABEL).to_be_visible()
        expect(self.pim_locators.SUPERVISOR_NAME_INPUT).to_be_visible()
        expect(self.pim_locators.JOB_TITLE_LABEL).to_be_visible()
        expect(self.pim_locators.JOB_TITLE_DROPDOWN).to_be_visible()
        expect(self.pim_locators.SUB_UNIT_LABEL).to_be_visible()
        expect(self.pim_locators.SUB_UNIT_DROPDOWN).to_be_visible()
        expect(self.pim_locators.QUESTION_LINK).to_be_visible()
        expect(self.pim_locators.RESET_BUTTON).to_be_visible()
        expect(self.pim_locators.SEARCH_BUTTON).to_be_visible()
        expect(self.pim_locators.RECORDS_COUNT).to_be_visible()

    def check_add_employee_page(self):
        expect(self.pim_locators.ADD_EMPLOYEE_TITLE).to_be_visible()
        expect(self.pim_locators.EMPLOYEE_FULL_NAME_TITLE).to_be_visible()
        expect(self.pim_locators.FIRST_NAME_FIELD).to_be_visible()
        expect(self.pim_locators.MIDDLE_NAME_FIELD).to_be_visible()
        expect(self.pim_locators.LAST_NAME_FIELD).to_be_visible()
        expect(self.pim_locators.EMPLOYEE_ID_TITLE).to_be_visible()
        expect(self.pim_locators.EMPLOYEE_ID_FIELD).to_be_visible()
        expect(self.pim_locators.ADD_PHOTO_BUTTON).to_be_visible()
        expect(self.pim_locators.PHOTO_HINT_TEXT).to_be_visible()
        expect(self.pim_locators.CREATE_LOGIN_TEXT).to_be_visible()
        expect(self.pim_locators.LOGIN_DETAILS_RADIOBUTTON).to_be_visible()
        expect(self.pim_locators.REQUIRED_TEXT).to_be_visible()
        expect(self.pim_locators.CANCEL_BUTTON).to_be_visible()
        expect(self.pim_locators.SAVE_BUTTON).to_be_visible()
