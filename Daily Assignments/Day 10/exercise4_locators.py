from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Edge browser
driver = webdriver.Edge()
driver.maximize_window()

# Open Amazon website
driver.get("https://www.amazon.in")

# Wait for page to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "navFooter"))
)

# Scroll to footer section
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Wait for footer to be visible
time.sleep(2)

# Click "About Us" safely
about_us = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='aboutamazon']"))
)
driver.execute_script("arguments[0].click();", about_us)  # JS click avoids interception

# Wait for next page
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Careers"))
)

# Find an element using LINK_TEXT
career_link = driver.find_element(By.LINK_TEXT, "Careers")
print("Text Found:", career_link.text)

# Close browser
driver.quit()
