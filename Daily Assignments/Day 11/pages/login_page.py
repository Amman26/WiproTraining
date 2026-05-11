from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.dashboard_page import DashboardPage

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.username_locator)).send_keys(username)
        self.driver.find_element(*self.password_locator).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        return DashboardPage(self.driver)