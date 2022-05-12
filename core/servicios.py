import json
import requests

def usoAPI():
    url = 'https://api-dolar-argentina.herokuapp.com/api/dolaroficial'
    r = requests.get(url)
    datos = r.json()
    return datos

def get_productos():
    url = 'http://localhost/webservicephp/controller/producto.php?REQUEST_METHOD=GET'
    resultado = requests.get(url)
    contactos = resultado.json()
    return contactos


def post_productos(dato):
    url = 'http://localhost/webservicephp/controller/producto.php?REQUEST_METHOD=POST'
    respuesta = requests.post(url, json = dato)
    return respuesta


def put_productos(dato):
    url = 'http://localhost/webservicephp/controller/producto.php?REQUEST_METHOD=PUT'
    respuesta = requests.put(url, json = dato)
    return respuesta    


def delete_productos(id):
    url = 'http://localhost/webservicephp/controller/producto.php?REQUEST_METHOD=DELETE' + str(id)
    respuesta = requests.delete(url)
    return respuesta   