from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Edge browser
driver = webdriver.Edge()
driver.maximize_window()

# Implicit wait
driver.implicitly_wait(10)

# Open Amazon website
driver.get("https://www.amazon.in")

# Search for Smart Watches
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Smart Watches")

# Click search button
driver.find_element(By.ID, "nav-search-submit-button").click()

# Explicit wait for search results
wait = WebDriverWait(driver, 15)
wait.until(
    EC.visibility_of_element_located((By.XPATH, "//div[@data-component-type='s-search-result']"))
)
print("Search results loaded")

# Expand brand filter section if needed
try:
    see_more = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='See more']"))
    )
    see_more.click()
    time.sleep(2)
except:
    print("No 'See more' link found, continuing...")

# Click Samsung brand filter
samsung_brand = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Samsung']"))
)
driver.execute_script("arguments[0].click();", samsung_brand)  # safer click
print("Samsung filter applied")

# Wait for page to refresh/update after filter
wait.until(
    EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Samsung')]"))
)

time.sleep(3)

# Count products displayed on first page
products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
print("Number of products displayed:", len(products))

# Close browser
driver.quit()
