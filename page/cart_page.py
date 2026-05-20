from selenium.webdriver.common.by import By
from page.base_page import BasePage

class CartPage(BasePage):

    CART_PRODUCTS = (By.CLASS_NAME,"inventory_item_name")


    def get_first_cart_product(self):

        return self.driver.find_elements(*self.CART_PRODUCTS)[0].text