from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', index, name="index"),
    path('get_all', views.get_all, name='get_all'),
    path('post_producto', views.post_producto, name='post_producto'),
    path('put_producto', views.put_producto, name='put_producto'),
    path('delete_producto', views.delete_producto, name='delete_producto'),
    path('usoAPI', views.usandoAPI, name='usoAPI'),
]