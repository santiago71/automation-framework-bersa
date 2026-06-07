from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.cart_page import CartPage
from page.login_page import LoginPage


class InventoryPage(BasePage):

    PRODUCTS_TITLE = (By.CLASS_NAME, "title")

    ADD_TO_CART_BUTTONS = (By.CLASS_NAME, "btn_inventory")

    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")

    MENU = (By.ID, "react-burger-menu-btn")

    FILTRO = (By.CLASS_NAME, "product_sort_container")

    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")

    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")

    PRODUCTS = (By.CLASS_NAME, "inventory_item")

    def get_title(self):

        return self.get_text(self.PRODUCTS_TITLE)

    def page_title(self):

        return self.driver.title

    def get_products(self):

        return self.find_elements(self.PRODUCTS)

    def add_first_product(self):

        self.find_elements(self.ADD_TO_CART_BUTTONS)[0].click()

    def get_cart_badge(self):

        return self.get_text(self.CART_BADGE)

    def open_cart(self):

        self.click(self.CART_BUTTON)
        self.wait.until(lambda d: "/cart.html" in d.current_url)
        return CartPage(self.driver)

    def get_first_product_title(self):

        return self.find_elements(self.PRODUCT_NAME)[0].text

    def button_menu(self):

        return self.find_element(self.MENU).is_displayed

    def filtro_visible(self):

        return self.find_element(self.FILTRO).is_displayed

    def add_product_to_cart(self, product_name):

        products = self.get_products()

        for product in products:

            name = product.find_element(*self.PRODUCT_NAME).text

            if name == product_name:

                product.find_element(*self.ADD_TO_CART_BUTTONS).click()

                break

    def get_product_info(self, product_name):

        products = self.get_products()

        for product in products:

            name = product.find_element(*self.PRODUCT_NAME).text

            if name == product_name:
                
                price = product.find_element(*self.PRODUCT_PRICE).text

                product.find_element(*self.PRODUCT_PRICE).text

                return {"name": name, "price": price}
            
        
