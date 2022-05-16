from django.db import models

# Create your models here.

class TipoProducto(models.Model):
    id_tipo_producto = models.IntegerField(primary_key =True, verbose_name = 'Id de tipo producto')
    nombreTipo = models.CharField(max_length = 50, verbose_name = 'Nombre del producto')

    def __str__(self):
        return self.nombreTipo


class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True, verbose_name='Id producto')
    nombreProducto = models.CharField(max_length=200, verbose_name='Nombre del producto')
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del producto')
    precio = models.IntegerField(verbose_name='Precio del producto')
    disponibilidad = models.IntegerField(verbose_name='Disponibilidad')
    tipo_producto = models.ForeignKey(TipoProducto, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.nombreProducto} -> {self.precio}'