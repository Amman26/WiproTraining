from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (By.ID, "loginusername")
    PASSWORD = (By.ID, "loginpassword")

    LOGIN_BUTTON = (By.XPATH, "//button[text()='Log in']")

    def login(self, username, password):

        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        )

        self.find(self.USERNAME).send_keys(username)

        self.find(self.PASSWORD).send_keys(password)

        self.click(self.LOGIN_BUTTON)

    def get_alert_text(self):

        wait = WebDriverWait(self.driver, 10)

        alert = wait.until(EC.alert_is_present())

        text = alert.text

        alert.accept()

        return text