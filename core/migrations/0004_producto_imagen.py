# Generated by Django 3.2.4 on 2022-05-16 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_producto_disponibilidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='core/sin-imagen.jpg', upload_to='core', verbose_name='Imagen del producto'),
        ),
    ]
