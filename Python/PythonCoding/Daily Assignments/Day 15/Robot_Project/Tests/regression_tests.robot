*** Settings ***
Library     SeleniumLibrary
Library     ../Libraries/ProductPage.py

Resource    ../Resources/common.resource
Resource    ../Resources/login_resources.resource

Suite Setup       Open Browser To SauceDemo
Suite Teardown    Close Browser Session
Test Teardown     Capture Failure Screenshot

*** Variables ***
${INVALID_ERROR}    Epic sadface: Username and password do not match any user in this service
${LOCKED_ERROR}     Epic sadface: Sorry, this user has been locked out.

*** Test Cases ***
Verify Product Price Total
    [Tags]    Regression    Critical

    Set Test Documentation
    ...    Verify total amount of two products.

    Login To Application    standard_user    secret_sauce

    ${price1}=    Get Product Price By Name    Sauce Labs Backpack
    ${price2}=    Get Product Price By Name    Sauce Labs Bike Light

    ${total}=    Evaluate    float(${price1}) + float(${price2})

    Should Be Equal As Numbers    ${total}    39.98


Invalid Login Scenarios
    [Template]    Invalid Login Scenario

    invalid_user      wrong_pass      ${INVALID_ERROR}
    locked_out_user   secret_sauce    ${LOCKED_ERROR}
    problem_user      wrong_pass      ${INVALID_ERROR}

*** Keywords ***
Invalid Login Scenario
    [Arguments]    ${username}    ${password}    ${expected_error}

    Go To    https://www.saucedemo.com

    Input Text        ${USERNAME_FIELD}    ${username}
    Input Password    ${PASSWORD_FIELD}    ${password}
    Click Button      ${LOGIN_BUTTON}

    Element Should Contain
    ...    xpath://h3[@data-test='error']
    ...    ${expected_error}