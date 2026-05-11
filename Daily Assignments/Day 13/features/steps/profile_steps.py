from behave import when
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


@when('I upload my new profile picture')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)

    # 1. Click the actual profile picture image to open the upload screen
    profile_pic = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "employee-image")))
    profile_pic.click()
    time.sleep(1)  # Wait for page to transition

    # 2. Now find the hidden file upload element
    upload_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))

    # 3. Send the file path
    absolute_file_path = os.path.abspath("test_data/profile_image.png")
    upload_element.send_keys(absolute_file_path)

    # 4. Click Save
    save_button = context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    save_button.click()