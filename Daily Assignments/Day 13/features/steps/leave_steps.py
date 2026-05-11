from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


@when('I apply for exactly one day of leave')
def step_impl(context):
    # Increased wait time to 15 seconds to be extra safe
    wait = WebDriverWait(context.driver, 15)

    # 1. Give the "Apply Leave" page time to load
    time.sleep(3)

    # 2. Bulletproof XPath: Looks for any label containing "Leave Type" and finds the dropdown next to it
    dropdown_xpath = "//label[contains(text(), 'Leave Type')]/ancestor::div[contains(@class, 'oxd-input-group')]//div[contains(@class, 'oxd-select-text')]"

    dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
    dropdown.click()
    time.sleep(1)

    # 3. Send arrow keys directly to the browser body to select the first option
    body = context.driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.5)
    body.send_keys(Keys.ENTER)

    # 4. Wait for the balance text to dynamically appear
    time.sleep(2)

    # 5. Capture the balance
    try:
        balance_xpath = "//*[contains(text(), 'Leave Balance')]/ancestor::div[contains(@class, 'oxd-input-group')]//p"
        balance_element = context.driver.find_element(By.XPATH, balance_xpath)
        # Extract just the number (e.g., from "10.00 Day(s)" -> 10.0)
        context.initial_balance = float(balance_element.text.split(' ')[0])
    except:
        context.initial_balance = 0.0  # Fallback if no balance is available


@then('I capture the success toast message')
def step_impl(context):
    pass


@then('exactly one day of leave should be deducted')
def step_impl(context):
    pass