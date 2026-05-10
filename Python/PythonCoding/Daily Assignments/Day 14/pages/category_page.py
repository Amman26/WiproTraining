import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.product_details_page import ProductDetailsPage


class CategoryPage(BasePage):

    PRODUCTS = (By.CSS_SELECTOR, ".card-title")

    def verify_laptop_list_presence(self):

        time.sleep(2)

        products = self.find_elements(self.PRODUCTS)

        assert len(products) > 0

    def get_all_product_names(self):

        time.sleep(2)

        products = self.find_elements(self.PRODUCTS)

        product_names = []

        for product in products:
            product_names.append(product.text)

        return product_names

    def click_product(self, product_name):

        time.sleep(2)

        product = (By.LINK_TEXT, product_name)

        self.click(product)

        return ProductDetailsPage(self.driver)