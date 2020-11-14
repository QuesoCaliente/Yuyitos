from django.db import models
from django.utils import timezone
from proveedor.models import Proveedor

# Create your models here.

class Familia(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre', unique = True, max_length = 100)
    codigo_familia = models.CharField('Codigo Familia',max_length = 100)

    class Meta:
        verbose_name = 'Familia'
        verbose_name_plural = 'Familias'

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre', max_length = 100)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre', max_length = 100)
    descripcion = models.TextField('Descripcion', max_length=255)
    familia = models.ForeignKey(Familia, verbose_name="Familia", on_delete=models.CASCADE)
    fecha_vencimiento = models.DateField('Fecha Vencimiento', auto_now=False, auto_now_add=False, default=timezone.now)
    precioCompra = models.IntegerField('Precio Compra')
    precioVenta = models.IntegerField('Precio Venta')
    marca = models.ForeignKey(Marca, verbose_name= 'Marca', on_delete=models.CASCADE)
    stock = models.IntegerField()
    codigo_producto = models.CharField('Codigo Producto', max_length=100, default='0')
    proveedor = models.ForeignKey(Proveedor, verbose_name="Proveedor", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['-id']

    def __str__(self):
        return self.nombre

