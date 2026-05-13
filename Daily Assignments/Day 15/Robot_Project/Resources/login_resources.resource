*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}                 https://www.saucedemo.com
${BROWSER}             Edge

${USERNAME_FIELD}      id:user-name
${PASSWORD_FIELD}      id:password
${LOGIN_BUTTON}        id:login-button

${PRODUCT_TITLE}       xpath://span[text()='Products']

*** Keywords ***
Login To Application
    [Arguments]    ${username}    ${password}

    Input Text      ${USERNAME_FIELD}    ${username}
    Input Password  ${PASSWORD_FIELD}    ${password}
    Click Button    ${LOGIN_BUTTON}