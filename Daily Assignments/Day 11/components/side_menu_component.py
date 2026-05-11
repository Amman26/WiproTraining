from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SideMenuComponent:
    def __init__(self, driver):
        self.driver = driver
        self.admin_menu = (By.XPATH, "//span[text()='Admin']")
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.leave_menu = (By.XPATH, "//span[text()='Leave']")

    def navigate_to_admin(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.admin_menu)).click()

    def navigate_to_pim(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.pim_menu)).click()

    def navigate_to_leave(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.leave_menu)).click()