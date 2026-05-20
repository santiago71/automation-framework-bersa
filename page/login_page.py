from selenium.webdriver.common.by import By

from page.base_page import BasePage


class LoginPage(BasePage):

    USERNAME_INPUT = (By.ID, "user-name")

    PASSWORD_INPUT = (By.ID, "password")

    LOGIN_BUTTON = (By.ID, "login-button")
    
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')


    def open_page(self):

        self.driver.get("https://www.saucedemo.com/")


    def enter_username(self, username):

        self.write(self.USERNAME_INPUT, username)


    def enter_password(self, password):

        self.write(self.PASSWORD_INPUT, password)


    def click_login(self):

        self.click(self.LOGIN_BUTTON)


    def login(self, username, password):

        self.open_page()

        self.enter_username(username)

        self.enter_password(password)

        self.click_login()
        
    def get_error_message(self):
        
        return self.get_text(self.ERROR_MESSAGE)        
