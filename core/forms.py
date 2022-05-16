from django import forms
from django .forms import ModelForm
from .models import Producto

#Crear la clase para el formulario

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['idProducto', 'nombreProducto', 'descripcion', 'imgProducto', 'precioProducto', 'categoria']