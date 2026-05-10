from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I navigate to the OrangeHRM login page')
def step_impl(context):
    target_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    context.driver.get(target_url)

@when('I login with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(username)
    context.driver.find_element(By.NAME, "password").send_keys(password)
    context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

@then('I should be logged in successfully')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.url_contains("dashboard"))
    assert "dashboard" in context.driver.current_url, f"Login failed. Current URL: {context.driver.current_url}"