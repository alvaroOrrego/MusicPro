from django.urls import path
from .views import tienda
from . import views

from .views import tienda, agregarProducto, eliminarProducto, restartProducto, limpiarCarrito

urlpatterns = [
    path('', tienda, name="tienda"),
    path('get_all', views.get_all, name='get_all'),
    path('post_producto', views.post_producto, name='post_producto'),
    path('put_producto', views.put_producto, name='put_producto'),
    path('delete_producto', views.delete_producto, name='delete_producto'),
    path('usoAPI', views.usandoAPI, name='usoAPI'),
    path('agregar/<int:id_producto>/', agregarProducto, name="add"),
    path('eliminar/<int:id_producto>/', eliminarProducto, name="delete"),
    path('restart/<int:id_producto>/', restartProducto, name="restart"),
    path('limpiar/', limpiarCarrito, name="cls"),
]