from behave import when
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('I enter "{first_name}" and "{last_name}"')
def step_impl(context, first_name, last_name):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.visibility_of_element_located((By.NAME, "firstName"))).send_keys(first_name)
    context.driver.find_element(By.NAME, "lastName").send_keys(last_name)

    # Explicit Wait to ensure the "Save" button is clickable
    save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    save_button.click()