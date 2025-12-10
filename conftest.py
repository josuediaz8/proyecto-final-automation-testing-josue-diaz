import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options

import pathlib
from datetime import datetime
import time

target = pathlib.Path("reports/screens")
target.mkdir(parents=True, exist_ok=True)

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox") #github
    options.add_argument("--disable-gpu") #github
    options.add_argument("--windows-size=1920,1080") #github
    options.add_argument("--handless=new") #github

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver,usuario,password):
    LoginPage(driver).abrir_pagina().login_completo(usuario,password)
    return driver

#URL de la API 
@pytest.fixture
def url_base():
    return "https://jsonplaceholder.typicode.com/"

#Para realizar capturas de pantalla automaticas al haber errores
@pytest.hookimpl(hookwrapper=True) #hookwrapper incorpora la captura de pantalla dentro del test
def pytest_runtest_makereport(item,call): #item es el test / call: ejecucion actual del test
    outcome = yield #pone en pausa la funcion y luego reanuda desde este punto

    report = outcome.get_result() #obtengo los resultados 

    if report.when in ("setup","call") and report.failed: #setup preparacion del test / Call ejecucion del test
        driver = item.funcargs.get("driver",None)
        
        if driver:
            timestamp_comun= datetime.now().strftime("%Y%m%d_%H%M%S")
            timestamp_unix = int(time.time())
            file_name= target / f"{report.when}_{item.name}_{timestamp_unix}.png" #nombre de la imagen
            driver.save_screenshot(str(file_name))