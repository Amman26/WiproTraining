from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from components.side_menu_component import SideMenuComponent


class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.sidebar = SideMenuComponent(self.driver)
        self.username_column_elements = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']/div[2]/div")

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h6[text()='Admin']"))
        )

    def verify_user_exists(self, target_username):
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(EC.presence_of_all_elements_located(self.username_column_elements))
        for element in elements:
            if element.text == target_username:
                return True
        return False