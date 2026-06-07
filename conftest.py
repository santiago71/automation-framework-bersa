import os

from datetime import datetime

import pytest
import pytest_html

from selenium import webdriver

from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
import os


@pytest.fixture
def driver():

    options = webdriver.ChromeOptions()

    options.add_argument("--incognito")
    # options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


@pytest.fixture
def login_p(driver):

    return LoginPage(driver)


@pytest.fixture
def inventory_page(driver):

    page = LoginPage(driver)

    page.login("standard_user", "secret_sauce")

    return InventoryPage(driver)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    extra = getattr(report, "extras", [])

    if report.when == "call":

        driver = item.funcargs.get("driver")

        if driver:

            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            status = "PASSED" if report.passed else "FAILED"

            screenshot_name = f"screenshots/" f"{item.name}_{status}_{timestamp}.png"

            driver.save_screenshot(screenshot_name)

            if os.path.exists(screenshot_name):

                html = f"""
                <div>
                    <p>{status}</p>
                    <img src="{screenshot_name}"
                    width="600">
                </div>
                """

                extra.append(pytest_html.extras.html(html))

        report.extras = extra
