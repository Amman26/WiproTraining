from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Edge browser
driver = webdriver.Edge()

# Maximize browser window
driver.maximize_window()

# Implicit Wait
driver.implicitly_wait(10)

# Open Amazon website
driver.get("https://www.amazon.in")

# Locate search bar
search_box = driver.find_element(By.ID, "twotabsearchtextbox")

# Enter laptop model
search_box.send_keys("Dell Inspiron 15")

# Click search button
driver.find_element(
    By.XPATH,
    "//input[@id='nav-search-submit-button']"
).click()

# Explicit Wait for first product image/result
wait = WebDriverWait(driver, 15)

first_product = wait.until(
    EC.visibility_of_element_located(
        (
            By.XPATH,
            "(//img[contains(@class,'s-image')])[1]"
        )
    )
)

print("Search results loaded successfully")

# Click first product
first_product.click()

print("First product clicked successfully")

# Wait for product page
time.sleep(3)

# Close browser
driver.quit()