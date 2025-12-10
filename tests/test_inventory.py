from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time
from utils.logger import logger

from pages.inventory_page import InventoryPage

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_inventory(login_in_driver,usuario,password):
    try:
        driver = login_in_driver
        inventory_page = InventoryPage(driver)

        # Verificar que hay productos
        logger.info(f"Validando que existen productos en la url: {driver .current_url}")

        assert len(inventory_page.obtener_todos_los_productos()) > 0, "El inventario esta vacio"
        
        logger.info(f"Cantidad de productos: {len(inventory_page.obtener_todos_los_productos())}")
        
        # Verificar vacio el carrito al inicio
        logger.info(f"Validando el carrito vacio")
        assert inventory_page.obtener_conteo_carrito() == 0

        # Agregar el primer producto
        logger.info(f"Agregando el primer producto al carrito")
        inventory_page.agregar_primer_producto()

        time.sleep(2)

        # Verificar el contador del carrito
        logger.info(f"Verificando el contador del carrito")
        assert inventory_page.obtener_conteo_carrito() == 10 #coloco 10 para que falle a proposito, debe ser 1
       
    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise
# Lo comento debido a que ya hace el driver.quit en el conftest y al intentar hacerlo 2 veces da "WARNING" en el reporte
#La prueba igual sale Ok pero para no tener ese WARNING lo quito
#     finally: 
#        driver.quit()