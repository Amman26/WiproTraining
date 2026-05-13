  *** Settings ***
Library    SeleniumLibrary

*** Variables ***
${ADD_BACKPACK}      id:add-to-cart-sauce-labs-backpack
${ADD_BIKELIGHT}     id:add-to-cart-sauce-labs-bike-light

${CART_ICON}         class:shopping_cart_link
${CART_BADGE}        class:shopping_cart_badge

${CHECKOUT_BUTTON}   id:checkout

*** Keywords ***
Add Backpack To Cart
    Click Button    ${ADD_BACKPACK}

Add Bike Light To Cart
    Click Button    ${ADD_BIKELIGHT}

Open Cart
    Click Element    ${CART_ICON}