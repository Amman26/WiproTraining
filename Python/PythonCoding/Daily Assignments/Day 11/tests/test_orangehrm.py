import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
#from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Import the Page Objects and Components
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from pages.pim_page import PIMPage
from components.side_menu_component import SideMenuComponent


# 1. Create a fixture to keep the browser open across multiple tests
@pytest.fixture(scope="module")
def driver():
    # Setup for Microsoft Edge
    service = EdgeService(executable_path="msedgedriver.exe")
    driver = webdriver.Edge(service=service)

    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()

    yield driver  # Hands the driver to the tests

    # Teardown: Closes browser after all tests in this file finish
    driver.quit()


# 2. Break the exercises into separate test functions
def test_exercises_1_and_2_login(driver):
    """Tests the POM Login and Dashboard Synchronization"""
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    assert "dashboard" in driver.current_url.lower(), "Failed to reach Dashboard"


def test_exercises_4_and_5_admin_data_driven(driver):
    """Tests Component Architecture and Data Driven Verification"""
    side_menu = SideMenuComponent(driver)
    side_menu.navigate_to_admin()

    admin_page = AdminPage(driver)
    user_exists = admin_page.verify_user_exists("Admin")
    assert user_exists is True, "Target user was not found in the Admin table."


def test_exercise_3_pim_chaining(driver):
    """Tests Multi-Page Navigation and Object Chaining"""
    # Exercise 3: Chaining and Multi-page
    side_menu =SideMenuComponent(driver)
    side_menu.navigate_to_pim()

    pim_page = PIMPage(driver)


    # 1. Look at the very first row in the table and grab the text from the "First Name" column
    first_name_locator = (By.XPATH, "(//div[@class='oxd-table-body']//div[@role='row'])[1]//div[@role='cell'][3]")
    wait = WebDriverWait(driver, 10)

    first_available_name = wait.until(EC.visibility_of_element_located(first_name_locator)).text

    print(f"\nDynamically found employee: {first_available_name}")

    # 2. Pass that name into your existing function
    personal_details = pim_page.view_employee_details(first_available_name)
    # ----------------------------

    assert personal_details is not None, "Failed to navigate to Personal Details"