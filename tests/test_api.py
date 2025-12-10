import requests



# Obtener usuario
def test_get_user(url_base):

    response = requests.get(f"{url_base}/users/1")

    assert response.status_code == 200

    data = response.json()

#Crear Usuario
def test_create_user(url_base):

    payload={
        "name": "Josue",
        "job": "Ingeniero"
    }
    response = requests.post(f"{url_base}/posts",json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == payload["name"]



# Eliminar usuario
def test_delete_user(url_base):
    response = requests.delete(f"{url_base}/posts/1")

    assert response.status_code == 200
