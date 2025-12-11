from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest


from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.lector_json import leer_json_productos

import time
from utils.logger import logger

RUTA_JSON = "datos/productos.json"

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
@pytest.mark.parametrize("nombre_producto",leer_json_productos(RUTA_JSON))
def test_cart_json(login_in_driver,usuario,password,nombre_producto):
    try:
        driver = login_in_driver
        inventory_page = InventoryPage(driver)

        # Agregar al carrito el producto
        logger.info(f"Agregando primer producto en test cart Json")
        inventory_page.agregar_producto_por_nombre(nombre_producto)

        # Abrir el carrito
        logger.info(f"Yendo a la pagina del carrito para validar el producto agregado. Test Cart Json")
        inventory_page.abrir_carrito()

        time.sleep(1)

        # Validar el producto
        cartPage = CartPage(driver)

        
        assert cartPage.obtener_nombre_producto_carrito() == nombre_producto
        logger.info(f"Obteniendo el nombre del producto en el carrito. Test Cart Json. Nombre: {cartPage.obtener_nombre_producto_carrito()}")

    except Exception as e:
        print(f"Error en test_cart: {e}")
        raise
    finally:
        driver.quit()


       