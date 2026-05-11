from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class PurchaseModal(BasePage):

    NAME = (By.ID, "name")
    COUNTRY = (By.ID, "country")
    CITY = (By.ID, "city")
    CARD = (By.ID, "card")
    MONTH = (By.ID, "month")
    YEAR = (By.ID, "year")

    PURCHASE = (By.XPATH, "//button[text()='Purchase']")

    @allure.step("Filling purchase form")
    def fill_purchase_form(self, data):

        with allure.step(f"Enter Name: {data['name']}"):
            self.find(self.NAME).send_keys(data["name"])

        with allure.step(f"Enter Country: {data['country']}"):
            self.find(self.COUNTRY).send_keys(data["country"])

        with allure.step(f"Enter City: {data['city']}"):
            self.find(self.CITY).send_keys(data["city"])

        with allure.step(f"Enter Card: {data['card']}"):
            self.find(self.CARD).send_keys(data["card"])

        with allure.step(f"Enter Month: {data['month']}"):
            self.find(self.MONTH).send_keys(data["month"])

        with allure.step(f"Enter Year: {data['year']}"):
            self.find(self.YEAR).send_keys(data["year"])

    def click_purchase(self):
        self.click(self.PURCHASE)