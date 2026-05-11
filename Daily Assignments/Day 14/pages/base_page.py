from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            15,
            ignored_exceptions=[StaleElementReferenceException]
        )

    def click(self, by_locator):
        element = self.wait.until(
            EC.element_to_be_clickable(by_locator)
        )
        element.click()

    def find(self, by_locator):
        return self.wait.until(
            EC.visibility_of_element_located(by_locator)
        )

    def find_elements(self, by_locator):
        return self.wait.until(
            EC.visibility_of_all_elements_located(by_locator)
        )

    def get_text(self, by_locator):
        return self.find(by_locator).text