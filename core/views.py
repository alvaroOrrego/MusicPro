from django.shortcuts import render, redirect

from django.http import HttpResponse
from .servicios import get_productos
from .servicios import post_productos
from .servicios import put_productos
from .servicios import delete_productos
from .servicios import usoAPI
from .carrito import Carrito
from .models import Producto


def index(request):
     return render(request, 'core/index.html')

def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'core/tienda.html', {'productos':productos})

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
    dato = { 'nombre': 'Guitarrita electriquita','descripcion': 'guitarra electrica terrible wena', 'precio': 109990, 'disponible': 1, 'TIPO_PRODUCTO_id': 1}
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

def index(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos':productos})

def agregarProducto(request, id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=id_producto)
    carrito.agregarCarrito(producto)
    return redirect("tienda")

def eliminarProducto(request, id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=id_producto)
    carrito.eliminarCarrito(producto)
    return redirect("tienda")

def restartProducto(request, id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=id_producto)
    carrito.restart(producto)
    return redirect("tienda")

def limpiarCarrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")