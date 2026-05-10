from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Edge browser
driver = webdriver.Edge()

# Open Amazon homepage
driver.get("https://www.amazon.in")

# Wait for page to load
time.sleep(3)

# Capture page title
title = driver.title
print("Page Title:", title)

# Verify title contains Amazon
assert "Amazon" in title
print("Title verification passed")

# Click on Mobiles category
driver.find_element(By.XPATH, "//a[contains(text(),'Mobiles')]").click()

# Wait for mobiles page
time.sleep(3)

print("Navigated to Mobiles page")

# Navigate back to homepage
driver.back()

time.sleep(3)

print("Returned to Home Page")

# Close browser
driver.quit()