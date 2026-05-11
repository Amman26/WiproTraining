from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Edge browser
driver = webdriver.Edge()

# Maximize browser
driver.maximize_window()

# Open Amazon website
driver.get("https://www.amazon.in")

# Wait for page to load
time.sleep(3)

# Locate search bar using ID
search_box = driver.find_element(By.ID, "twotabsearchtextbox")

# Enter product name
search_box.send_keys("Wireless Headphones")

# Locate search button using XPath
search_button = driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")

# Click search button
search_button.click()

# Wait for search results page
time.sleep(3)

# Capture page source/text
page_text = driver.page_source

# Verify results are displayed
assert "Wireless Headphones" in page_text

print("Search results displayed successfully")

# Close browser
driver.quit()