import os
import pytest
import allure

from selenium import webdriver


@pytest.fixture
def driver():

    driver = webdriver.Edge()

    driver.maximize_window()

    driver.get("https://www.demoblaze.com/index.html")

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["driver"]

        os.makedirs("screenshots", exist_ok=True)

        screenshot_path = f"screenshots/{item.name}.png"

        driver.save_screenshot(screenshot_path)

        with open(screenshot_path, "rb") as file:
            allure.attach(
                file.read(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )