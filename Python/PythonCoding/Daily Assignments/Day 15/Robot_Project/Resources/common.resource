 *** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open Browser To SauceDemo
    Open Browser    https://www.saucedemo.com    Edge
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

Close Browser Session
    Close Browser

Capture Failure Screenshot
    ${timestamp}=    Get Time    epoch
    Run Keyword If Test Failed
    ...    Capture Page Screenshot
    ...    failure_${TEST_NAME}_${timestamp}.png