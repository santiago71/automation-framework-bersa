from selenium.webdriver.common.by import By

from page.base_page import BasePage


class LoginPage(BasePage):

    USERNAME_INPUT = (By.ID, "username")

    CONTINUE_BUTTON = (By.ID, "global.continue")

    PASSWORD_INPUT = (By.ID, "password")

    LOGIN_BUTTON = (By.ID, "global.getInto")

    LOGIN_FAILED = (By.CSS_SELECTOR, "notification-message")

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

    def get_error_message(self):

        element = self.find_element(self.LOGIN_FAILED)
        message = element.text
        return message
