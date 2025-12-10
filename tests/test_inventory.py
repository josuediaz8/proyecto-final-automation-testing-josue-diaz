from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time

from pages.inventory_page import InventoryPage

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_inventory(login_in_driver,usuario,password):
    try:
        driver = login_in_driver
        inventory_page = InventoryPage(driver)

        # Verificar que hay productos
        assert len(inventory_page.obtener_todos_los_productos()) > 0, "El inventario esta vacio"

        # Verificar vacio el carrito al inicio
        assert inventory_page.obtener_conteo_carrito() == 0

        # Agregar el primer producto
        inventory_page.agregar_primer_producto()

        time.sleep(2)

        # Verificar el contador del carrito
        assert inventory_page.obtener_conteo_carrito() == 1
       
    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise
# Lo comento debido a que ya hace el driver.quit en el conftest y al intentar hacerlo 2 veces da "WARNING" en el reporte
#La prueba igual sale Ok pero para no tener ese WARNING lo quito
#     finally: 
#        driver.quit()