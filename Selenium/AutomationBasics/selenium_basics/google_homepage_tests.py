""""code for google page testing"""

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#browser = input('What browser you want to use. edge/chrome ')



# Set up Edge driver using WebDriver Manager
match (browser.lower()):
    case 'chrome':

        driver_path = r"C:\Wipro Training\Selenium\AutomationBasics\resources\chromedriver.exe"
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service)
    case 'edge':
        driver_path = r"C:\Wipro Training\Selenium\AutomationBasics\resources\msedgedriver.exe"
        service = Service(driver_path)
        driver = webdriver.Edge(service=service)




# Open Google
driver.get("https://www.google.com")

# Optional: print the page title to confirm
pagetitle=driver.title

if pagetitle == 'Google':
    print("Google homepage loaded - pass")
else:
    print("Google homepage not laoded - fail")


import time

time.sleep(5)

driver.quit()

# Close the browser after a short delay