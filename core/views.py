from django.shortcuts import render

from django.http import HttpResponse
from .servicios import get_productos
from .servicios import post_productos
from .servicios import put_productos
from .servicios import delete_productos
from .servicios import usoAPI


def index(request):
     return render(request, 'core/index.html')

# API USD:
def usandoAPI(request):
    context = {
        'apiDolar': usoAPI()
    }
    return render(request, 'core/apiUsd.html', context)


def get_all(request):
    context = {
        'lista' : get_productos()  
    }          
    return render(request, 'core/get.html', context)


def post_producto(request):
    dato = { 'descripcion': 'guitarra electrica terrible wena', 'precio': 109990, 'disponible': 1, 'TIPO_PRODUCTO_id': 1}
    context = {
        'mensaje': post_productos(dato)
    }
    return render(request, 'post.html', context)


def put_producto(request):
    dato = {'id_producto': '1','descripcion': 'guitarra electrica terrible wenaXXX', 'precio': 112990, 'disponible': 2, 'TIPO_PRODUCTO_id': 1}
    context = {
        'mensaje': put_productos(dato)
    }
    return render(request, 'put.html', context)


def delete_producto(request):
    id = 1
    context = {
        'mensaje': delete_productos(id)
    }
    return render(request, 'delete.html', context)    
    