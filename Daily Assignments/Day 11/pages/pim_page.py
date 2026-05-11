from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PersonalDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.personal_details_header = (By.XPATH, "//h6[text()='Personal Details']")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.personal_details_header)
        )

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.employee_record_xpath = "//div[contains(@class, 'oxd-table-row')]//div[contains(text(), '{}')]"

    def view_employee_details(self, name):
        dynamic_locator = (By.XPATH, self.employee_record_xpath.format(name))
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(dynamic_locator))
        element.click()
        return PersonalDetailsPage(self.driver)