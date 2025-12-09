import pytest
import datetime

# Lista de archivos de pruebas a ejecutar
test_files = [
 #   "tests/test_login.py",
  #  "tests/test_inventory.py",
    "tests/test_cart.py",
    "tests/test_api.py"
]

#Armo estructura de fecha para Reporte
now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") 

# Argumentos para ejecutar las pruebas: archivos + reporte HTML
pytest_args = test_files + [f"--html=report-{now}.html", "--self-contained-html", "-v"]


pytest.main(pytest_args)