import time

import pytest
from pytest_check import check
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.google.com')
    yield driver
    driver.quit()

def test_ghp(driver):
    pagetitle = driver.title
    assert pagetitle == 'Google','Google home page NOT LOADED!!'

def test_image_page_loaded(driver):
    driver.find_element(By.LINK_TEXT,'Images').click()
    pagetitle = driver.title
    assert pagetitle == 'Google Images','Image page NOT LOADED!'

def test_business_page(driver):
    driver.find_element(By.LINK_TEXT,'Business').click()
    # time.sleep(1)
    wait = WebDriverWait(driver,5)
    wait.until(EC.title_contains('Business'))
    # assert 'Business' in driver.title,'Business page NOT loaded -- title check'
    # assert 'business' in driver.current_url,'Business page NOT loaded -- url check'

#  for checking two or more failures
    check.equal('business',driver.title,'Business page NOT loaded -- title check')
    check.is_in('business', driver.current_url, 'Business page NOT loaded -- URL check')