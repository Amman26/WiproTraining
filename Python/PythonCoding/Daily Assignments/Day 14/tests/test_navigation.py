from pages.home_page import HomePage


def test_navigation_to_laptops(driver):

    home = HomePage(driver)

    home.click_laptops().verify_laptop_list_presence()
