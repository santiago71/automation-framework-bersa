from page.cart_page import CartPage
from utils.assertions import assert_equal

def test_product_added_to_cart(inventory_page):

    product_title = inventory_page.get_first_product_title()

    inventory_page.add_first_product()

    cart_page = inventory_page.open_cart()

    cart_product = cart_page.get_first_cart_product()

    assert product_title == cart_product, "El producto del carrito no coincide con el agregado"