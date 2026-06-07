from selenium.webdriver.common.by import By
import time
from page.base_page import BasePage


class LoginPage(BasePage):
    
    #LOCATORS

    USERNAME_INPUT = (By.ID, "username")

    CONTINUE_BUTTON = (By.ID, "global.continue")

    PASSWORD_INPUT = (By.ID, "password")

    LOGIN_BUTTON = (By.ID, "global.getInto")

    LOGIN_FAILED = (By.XPATH, "//*[contains(@class,'notification')]")

    CAPTCHA_IFRAME = (By.XPATH, "//iframe[contains(@title,'reCAPTCHA')]")

    def open_page(self):

        self.driver.get("https://betest01.bancoentrerios.com/loginStep1")

    def enter_username(self, username):

        self.write(self.USERNAME_INPUT, username)

    def continue_user(self):

        self.click(self.CONTINUE_BUTTON)

    def enter_password(self, password):

        self.write(self.PASSWORD_INPUT, password)

    def click_login(self):

        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):

        self.open_page()

        self.enter_username(username)

        self.continue_user()

        self.enter_password(password)

        self.click_login()

        self.wait.until(lambda driver: ("/desktop" in driver.current_url or self.has_error_text() or self.is_captcha_present()))

    def has_error_text(self):

        try:

            element = self.driver.find_element(*self.LOGIN_FAILED)

            return element.text.strip() != ""

        except Exception:

            return False

    def get_error_message(self):

        elements = self.driver.find_elements(*self.LOGIN_FAILED)

        if elements:
            return elements[0].text.strip()

        return ""
    

    def is_captcha_present(self):

        return self.element_exists(self.CAPTCHA_IFRAME)

    def is_login_succesfull(self):
        
        return "/desktop" in self.driver.current_url