from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_heading = (By.XPATH, "//h6[contains(., 'Dashboard')]")
        self._verify_page_loaded()

    def _verify_page_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.dashboard_heading)
        )