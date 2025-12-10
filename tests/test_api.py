import requests
from utils.logger import logger


# Obtener usuario - GET
def test_get_user(url_base):

    logger.info(f"Relizando la solitud GET a {url_base} ")

    response = requests.get(f"{url_base}/users/1")

    logger.info(f"Status code GET: {response.status_code}")
    assert response.status_code == 200

    data = response.json()
    
    logger.info("Validando el id dentro del response")
    assert data["id"] == 1

#Crear Usuario - POST
def test_create_user(url_base):
    logger.info(f"Relizando la solitud POST a {url_base}/posts")
    payload={
        "name": "Josue",
        "job": "Ingeniero"
    }
    response = requests.post(f"{url_base}/posts",json=payload)

    logger.info(f"Status code POST: {response.status_code}")
    assert response.status_code == 201

    data = response.json()
    
    logger.info("Validando el 'NAME' dentro del response")
    assert data["name"] == payload["name"]



# Eliminar usuario - DELETE
def test_delete_user(url_base):
    logger.info(f"Relizando la solitud DELETE a {url_base}/posts/1")    
    response = requests.delete(f"{url_base}/posts/1")

    logger.info(f"Status code DELETE: {response.status_code}")
    assert response.status_code == 200
