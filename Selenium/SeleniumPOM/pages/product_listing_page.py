from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductListingPage:

    PRODUCT_TITLES = (By.CSS_SELECTOR, "a h2 span")
    BRAND_FILTER = (By.XPATH, "//span[text()='Logitech']/parent::a/descendant::i")



    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def find_product_title(self):
        first_product = (  EC.visibility_of_element_located(self.PRODUCT_TITLES) )
        print("\nFirst Product:", first_product.text)


    def all_product(self):
        product_title = self.wait.until(  EC.presence_of_all_elements_located(self.PRODUCT_TITLES)  )
        print(f"\nFound {len(product_title)} product titles on page one.\n")

        for i, title in enumerate(product_title[:5], start=1):
            print(f"{i}. {title.text}")

        return len(product_titles) > 0

    def select_brand_filter(self):
        brand_filter = self.driver.find_element(*self.BRAND_FILTER)
        brand_filter.click()

    def check_product_titles_for_brand_filter(self, brandname):
        product_title = self.wait.until(  EC.presence_of_all_elements_located(self.PRODUCT_TITLES)  )

        for title in product_titles:
            if not title.text.__contains__(brandname):
                return False
        return True


