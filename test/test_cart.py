from page.cart_page import CartPage
from utils.assertions import assert_equal
from utils.data_reader import read_json


def test_product_added_to_cart(inventory_page):

    product_title = inventory_page.get_first_product_title()

    inventory_page.add_first_product()

    cart_page = inventory_page.open_cart()

    cart_product = cart_page.get_first_cart_product()

    assert (
        product_title == cart_product
    ), "El producto del carrito no coincide con el agregado"


def test_products_inventory_and_cart(inventory_page):

    expected_products = read_json("data/products.json")

    inventory_products = []

    for product in expected_products:

        inventory_page.add_product_to_cart(product["name"])

        inventory_info = inventory_page.get_product_info(product["name"])

        inventory_products.append(inventory_info)

        assert inventory_info == product

        inventory_page.take_screenshot("products_added_to_cart")

    inventory_page.open_cart()

    cart_page = CartPage(inventory_page.driver)

    cart_products = cart_page.get_cart_products()

    cart_page.take_screenshot("cart_products")

    for product in expected_products:

        assert product in cart_products, (
            f"Producto incorrecto en el carrito:" f"{product['name']}"
        )
