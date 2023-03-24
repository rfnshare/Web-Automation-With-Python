from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage
from utilities.data import SampleData


class CheckOutPage:
    all_products_loc = (By.XPATH, "//h4/a")
    product = (By.XPATH, "ancestor::div[@class='card h-100']//button")

    def __init__(self, driver):
        self.driver = driver

    def add_products(self):
        # Adding Product Into Cart
        all_products = self.driver.find_elements(*CheckOutPage.all_products_loc)
        for product in all_products:
            if product.text in SampleData.product_list:
                product.find_element(*CheckOutPage.product).click()  # Chaining Web Elements

    def go_to_checkout(self):
        # Go To Checkout Page
        home = HomePage(self.driver)
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Checkout").click()
        home.wait_for_an_element((By.CSS_SELECTOR, ".btn-success"))  # Waiting for Checkout Button In Next Page

    def confirm_checkout(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".btn-success")
