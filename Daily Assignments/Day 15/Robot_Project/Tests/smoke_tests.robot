*** Settings ***
Resource    ../Resources/common.resource
Resource    ../Resources/login_resources.resource

Suite Setup       Open Browser To SauceDemo
Suite Teardown    Close Browser Session
Test Teardown     Capture Failure Screenshot

*** Test Cases ***
Valid Login Test
    [Tags]    Critical    Smoke    Regression

    Set Test Documentation
    ...    Verify successful login into SauceDemo application.

    Login To Application    standard_user    secret_sauce

    Wait Until Element Is Visible    ${PRODUCT_TITLE}

    Element Should Be Visible    ${PRODUCT_TITLE}