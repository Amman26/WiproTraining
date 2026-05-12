from selenium.webdriver.common.by import By

class ProductPage:

    def __init__(self):
        self.prices = {
            "Sauce Labs Backpack": "29.99",
            "Sauce Labs Bike Light": "9.99"
        }

    def get_product_price_by_name(self, product_name):
        return self.prices[product_name]