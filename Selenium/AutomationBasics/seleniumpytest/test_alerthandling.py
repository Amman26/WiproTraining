import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://the-internet.herokuapp.com/javascript_alerts')
    yield driver
    driver.quit()
# ---------------------ALERT-----------------------
def test_simple_js_alert(driver):
    driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
    alert = driver.switch_to.alert
    assert alert.text == 'I am a JS Alert','Alert check was wrong'
    time.sleep(3)
    alert.accept()

    time.sleep(3)
    result = driver.find_element(By.ID,'result').text
    assert "You successfully clicked an alert" in result, 'Result text was wrong'

# ------------------------CONFIRM DISMISS -------------------------------
def test_simple_js_confirmdismiss(driver):
    driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
    alert = driver.switch_to.alert
    assert alert.text == 'I am a JS Confirm','Alert check was wrong'
    alert.dismiss()
    time.sleep(3)
    result = driver.find_element(By.ID,'result').text
    assert "You clicked: Cancel" in result, 'Result text was wrong'

# -------------------------------- CONFIRM OK---------------------------
def test_simple_js_confirm(driver):
    driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
    alert = driver.switch_to.alert
    assert alert.text == 'I am a JS Confirm','Confirm check was wrong'
    time.sleep(3)
    alert.accept()

    time.sleep(3)
    result = driver.find_element(By.ID,'result').text
    assert "You clicked: Ok" in result, 'Result text was wrong'
# --------------------------- PROMPT --------------------------------
def test_simple_js_prompt(driver):
    driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
    alert = driver.switch_to.alert
    assert alert.text == 'I am a JS prompt','Alert text was wrong'
    alert.send_keys("Python Selenium")
    time.sleep(3)
    alert.accept()

    time.sleep(3)
    result = driver.find_element(By.ID,'result').text
    assert "Python Selenium" in result, 'Result text was wrong'
# -----------------------------------------------------------