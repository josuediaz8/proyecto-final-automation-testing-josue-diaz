# Proyecto de Talento Tech

## Propósito del proyecto

El objetivo del proyecto es automatizar las pruebas UI para el sitio **SauceDemo**, y de la API **JsonPlaceHolder**. Aplicando practicas como Page Object Model, manejo de datos externos generacion de reportes, logging, capturas de pantalla.
Utilizando tecnologias como Pytest, Selenium, generar reportes HTMLs, etc.

En este proyecto se automatizan las siguientes pruebas:
- Sitio web:  https://www.saucedemo.com/
- Ingreso al login
- Validar que existan articulos disponibles
- Validar que se pueda agregar un producto al carrito
- Validar que se incremente el carrito de compra
- Validar que el producto agregado al carrito sea el correcto

## Tecnologías utilizadas

- Visual Studio Code: editor de código fuente gratuito, ligero y potente que se ejecuta en Windows, macOS y Linux.
- Python: Lenguaje de programación utilizado para crear scripts que ejecutan pruebas automáticamente en aplicaciones de software, en lugar de realizar el proceso manualmente
- Selenium WebDriver: Herramienta para automatizar pruebas de navegadores web, permitiendo simular acciones del usuario real.
- Pytest: Framework de pruebas en Python que facilita la escritura y ejecución de casos de prueba automáticos.
- Faker:
- CSV /JSON


## Instrucciones de instalación de dependencias

- Visual Studio Code: desde https://code.visualstudio.com/download
- Python: https://www.python.org/downloads/
- Pytest: Dentro del Visual Studio Code, abra su terminal o símbolo del sistema, ejecute el comando: pip install pytest
- Selenium: Dentro del Visual Studio Code, abra su terminal o símbolo del sistema,ejecuta el comando: pip install selenium
- Generacion de Reportes: Dentro del Visual Studio Code, abra su terminal o símbolo del sistema, ejecuta el comando: pip install pytest-htm


## Reportes y Logs

El proyecto genera tres tipos principales de resultados durante la ejecucion de las prubas: **reporte HTML**, **capturas de pantalla**, **archivo de log**

### Reporte HTML
Se genera un reporte HTML detallado con el nombre de ```report-Y-m-D_H-M-S.hmtl``` en la **carpeta raiz** del proyecto

### Logs de ejecución
Tambien se genera un log con informacion detallada de toda la ejecución de las pruebas en la siguiente ubicacion: ```logs/suite.log```

### Capturas de pantalla

Se realizan capturas de pantalla por cada test que haya fallado y se encuentran en la siguiente ubicacion: ```reports/screens/```

## Ejuctar todas las pruebas
Para iniciar la ejecucion de las pruebas debes ejecutar la siguiente linea:

```bash
python -m run_test.py
```

Tambien se puede ejecutar cada prueba por separado ejecutando cada comando:
```bash
py -m pytest -v .\tests\test_login.py
```
```bash
py -m pytest -v .\tests\test_navegacion.py
```
```bash
py -m pytest -v .\tests\test_carrito.py
```

## ¿Como interpretar los reportes?
- Al ejecutar `run_test.py`, se genera un archivo HTML en la carpeta raiz.
- El reporte incluye:
    - Lista completa de test ejecutados
    - El estado de cada prueba
    - La duracion de cada test
    - Las capturas de pantalla para pruebas fallidas

## Pruebas incluidas
- Login exitoso y fallido
- Login exitoso y fallido usando faker
- Comportamiento de la pagina de inventario
- Comportamiento de la pagina del carrito
- API (Reqres): GET users, POST create user, DELETE user, validaciones de codigos HTTP, validaciones de estructura JSON

## Manejo de datos de prueba
- En la carpeta `datos` se incluyen archivos como:
    - `data_login.csv` -> datos de usuarios validos o invalidos
    - `productos.json` -> datos de productos para validacion

### Conclusion
Este proyecto ofrece una estructura organizada y escalable para automatizar pruebas de API utilizando Python y Pytest. Incluye un flujo simple de ejeucion mediante `run_test.py`, generacion automatica de reporte HTML facilitando el analisis de las pruebas.

La arquitectura del proyecto esta pensada para agregar nuevos casos de prueba y configuraciones sin modificar el nucleo del proyecto, manteniendo buenas practicas y permitiendo su escalabilidad en el tiempo.


👤 **Autor**
- Josue Diaz
- GitHub: https://github.com/josuediaz8/
