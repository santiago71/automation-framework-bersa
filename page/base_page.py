from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


class BasePage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):

        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def write(self, locator, text):

        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):

        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def find_element(self, locator):

        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):

        return self.driver.find_elements(*locator)

<<<<<<< HEAD
    def wait_homepage(self):

        self.wait.until(EC.url_contains("/desktop"))

    def element_exists(self, locator):

        elements = self.driver.find_elements(*locator)

        return len(elements) > 0

=======
>>>>>>> 0f9283e4534d9b48374b38c66ecf84388efd46ef
    def take_screenshot(self, name):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        self.driver.save_screenshot(f"screenshots/{name}_{timestamp}.png")
<<<<<<< HEAD

    def wait_for_text_in_element(self, locator):

        self.wait.until(lambda driver: self.get_text(locator).strip() != "")
=======
>>>>>>> 0f9283e4534d9b48374b38c66ecf84388efd46ef
