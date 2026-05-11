from behave import when
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@when('I navigate to the "{menu_name}" menu')
def step_impl(context, menu_name):
    wait = WebDriverWait(context.driver, 10)
    # This clicks the items on the left side panel (Admin, PIM, Leave, My Info)
    menu = wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{menu_name}']")))
    menu.click()
    time.sleep(1) # Brief pause to allow the new page to load

@when('I click on the "{tab_name}" tab')
def step_impl(context, tab_name):
    wait = WebDriverWait(context.driver, 10)
    # This clicks the top navigation tabs (like 'Add Employee' or 'Apply')
    tab = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{tab_name}']")))
    tab.click()
    time.sleep(1)