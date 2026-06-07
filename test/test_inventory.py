from utils.assertions import assert_equal


def test_page_title(inventory_page):

    title = inventory_page.page_title()

    inventory_page.take_screenshot("Titulo_correcto_Swag_Labs")

    assert title == "Swag Labs", "Titulo del navegador es incorrecto"


def test_inventory_title(inventory_page):

    title = inventory_page.get_title()

    inventory_page.take_screenshot("Titulo_visual_Products")

    assert title == "Products", "Titulo visual del inventario es incorrecto"


def test_boton_menu(inventory_page):

    inventory_page.take_screenshot("boton_menu_visible")

    assert inventory_page.button_menu(), "El boton no es visible"


def test_filtro(inventory_page):

    inventory_page.take_screenshot("filtro_visible")

    assert inventory_page.filtro_visible(), "El filtro no es visible"


def test_products_displayed(inventory_page):

    products = inventory_page.get_products()

    inventory_page.take_screenshot("productos_visibles")

    assert len(products) > 0, "No hay productos visibles en el inventario"


def test_add_product_to_cart(inventory_page):

    inventory_page.add_first_product()

    inventory_page.take_screenshot("producto_agregado_carrito")

    cart_badge = inventory_page.get_cart_badge()

    assert_equal(cart_badge, "1", "El carrito no actualizo correctamente")
