import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.amazon.in")

    # Use explicit wait instead of time.sleep
    wait = WebDriverWait(driver, 5)
    try:
        # Try to click "Continue shopping" if it exists
        continue_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue shopping')]"))
        )
        continue_btn.click()
    except Exception:
        # If not found, just skip gracefully
        print("No 'Continue shopping' button found, continuing without clicking.")

    yield driver
    driver.quit()
