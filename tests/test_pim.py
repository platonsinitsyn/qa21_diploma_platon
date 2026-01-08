import pytest


@pytest.mark.smoke
def test_check_employee_list_page(logged_in, pim_page):
    pim_page.click_pim_tab()
    pim_page.check_employee_list_page()


@pytest.mark.smoke
def test_check_add_employee_page(logged_in, pim_page):
    pim_page.click_pim_tab()
    pim_page.click_add_employee_tab()
    pim_page.check_add_employee_page()


@pytest.mark.smoke
def test_add_new_employee(logged_in, pim_page):
    pim_page.click_pim_tab()
    pim_page.click_add_employee_tab()
    pim_page.enter_employee_data("John", "Stuart", "Smith")
    pim_page.click_save_button()
    pim_page.check_new_employee_is_created()


@pytest.mark.smoke
@pytest.mark.parametrize(
    "field_name,value,field_type,check_table",
    [
        ("EMPLOYEE_NAME_INPUT", "divya 123", "input", False),
        ("EMPLOYEE_ID_INPUT", "6969", "input", False),
        ("EMPLOYMENT_STATUS_DROPDOWN", "Full-Time Permanent", "dropdown", False),
        ("INCLUDE_DROPDOWN", "Current and Past Employees", "dropdown", False),
        ("SUPERVISOR_NAME_INPUT", "John", "input", False),
        ("JOB_TITLE_DROPDOWN", "HR Manager", "dropdown", False),
        ("SUB_UNIT_DROPDOWN", "Human Resources", "dropdown", False),
    ],
)
def test_fill_pim_filters(logged_in, pim_page, field_name, value, field_type, check_table):
    pim_page.click_pim_tab()
    field = getattr(pim_page.pim_locators, field_name)
    if field_type == "input":
        pim_page.fill_and_check_input(field, value)
    else:
        pim_page.select_and_check_dropdown(field, value)
    pim_page.click_search_button()
    if check_table:
        pim_page.row_with_text_should_be_visible(value)
