import pytest
import datetime


#Armo estructura de fecha para Reporte
now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") 

# Argumentos para ejecutar las pruebas: archivos + reporte HTML
#pytest_args = test_files + [f"--html=report-{now}.html", "--self-contained-html", "-v"]


pytest.main(["tests/",f"--html=reports/report-{now}.html", "--self-contained-html", "-v"])