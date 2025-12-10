from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_cart(login_in_driver,usuario,password):
    try:
        driver = login_in_driver
        inventory_page = InventoryPage(driver)

        # Agregar al carrito el producto
        inventory_page.agregar_primer_producto()

        # Abrir el carrito
        inventory_page.abrir_carrito()

        # Validar el producto
        cartPage = CartPage(driver)
        
        productos_en_carrito = cartPage.obtener_productos_carrito()
        assert len(productos_en_carrito) == 1

    except Exception as e:
        print(f"Error en test_cart: {e}")
        raise
# Lo comento debido a que ya hace el driver.quit en el conftest y al intentar hacerlo 2 veces da "WARNING" en el reporte
#La prueba igual sale Ok pero para no tener ese WARNING lo quito
#     finally: 
#        driver.quit()