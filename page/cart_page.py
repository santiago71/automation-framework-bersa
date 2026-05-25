from selenium.webdriver.common.by import By
from page.base_page import BasePage


class CartPage(BasePage):

    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")

    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def get_first_cart_product(self):

        return self.driver.find_elements(*self.PRODUCT_NAME)[0].text

    def get_cart_products(self):

        items = self.find_elements(self.CART_ITEMS)

        products = []

        for item in items:

            name = item.find_element(*self.PRODUCT_NAME).text

            price = item.find_element(*self.PRODUCT_PRICE).text

            products.append({"name": name, "price": price})

        return products
                   
    