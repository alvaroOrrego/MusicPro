from django.urls import path
from .views import tienda
from . import views

from .views import tienda, agregarProducto, agregarProducto2, eliminarProducto, restartProducto, restartProducto2, limpiarCarrito, limpiarCarrito2#, dctar

urlpatterns = [
#   path('', tienda, name="tienda"),
    path('', views.tienda, name='tienda'),
    path('todoTienda', views.todoTienda, name='todoTienda'),
    path('post_producto', views.post_producto, name='post_producto'),
    path('put_producto', views.put_producto, name='put_producto'),
    path('delete_producto', views.delete_producto, name='delete_producto'),
    path('usoAPI', views.usandoAPI, name='usoAPI'),
    path('agregar/<int:id_producto>/', agregarProducto, name="add"),
    path('agregar2/<int:id_producto>/', agregarProducto2, name="add2"),
    path('eliminar/<int:id_producto>/', eliminarProducto, name="delete"),
    path('restart/<int:id_producto>/', restartProducto, name="restart"),
    path('restart2/<int:id_producto>/', restartProducto2, name="restart2"),
    path('limpiar/', limpiarCarrito, name="cls"),
    path('limpiar2/', limpiarCarrito2, name="cls2"),
    #path('dcto', dctar, name="dcto"),
]