from behave import when
from selenium.webdriver.common.by import By


@when('I enter the following search criteria:')
def step_impl(context):
    # Iterate through the dictionary provided by the data table
    for row in context.table:
        username = row.get("Username")
        user_role = row.get("User Role")
        status = row.get("Status")

        if username:
            context.driver.find_element(By.XPATH,
                                        "//label[text()='Username']/../following-sibling::div/input").send_keys(
                username)

        if user_role:
            pass  # Implement Dropdown logic for User Role

        if status:
            pass  # Implement Dropdown logic for Status