from pages.home_page import HomePage
from pages.category_page import CategoryPage
from pages.cart_page import CartPage


def test_checkout(driver):

    home = HomePage(driver)

    category = home.click_laptops()

    product_page = category.click_product("Sony vaio i5")

    product_page.add_product_to_cart()

    home.click_cart()

    cart = CartPage(driver)

    modal = cart.click_place_order()

    data = {
        "name": "Amman",
        "country": "India",
        "city": "Delhi",
        "card": "123456789",
        "month": "May",
        "year": "2026"
    }

    modal.fill_purchase_form(data)

    modal.click_purchase()

    assert "Thank you for your purchase!" in cart.get_success_message()