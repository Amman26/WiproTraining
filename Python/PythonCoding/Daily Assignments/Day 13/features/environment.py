from selenium import webdriver
import os


# Challenge: Implement Cucumber Hooks (@Before and @After)[cite: 28].
def before_scenario(context, scenario):
    """
    The @Before hook should maximize the browser[cite: 29].
    In Python's behave framework, this is handled by before_scenario.
    """
    context.driver = webdriver.Edge()
    context.driver.maximize_window()


def after_scenario(context, scenario):
    """
    The @After hook should take a screenshot if the scenario fails before quitting the driver[cite: 29].
    """
    if scenario.status == "failed":
        screenshot_name = f"{scenario.name.replace(' ', '_')}_failed.png"
        context.driver.save_screenshot(screenshot_name)

    context.driver.quit()