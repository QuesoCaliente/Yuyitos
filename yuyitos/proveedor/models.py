from django.db import models

# Create your models here.

class Rubro(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre', max_length=50)

    class Meta:
        verbose_name = 'Rubro'
        verbose_name_plural = 'Rubros'

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    id = models.AutoField(primary_key = True)
    rut = models.CharField('Rut', max_length=12)
    nombre = models.CharField('Nombre', max_length=50)
    correo = models.EmailField('Correo', max_length=254)
    telefono = models.IntegerField('Telefono')
    direccion = models.CharField('Direccion', max_length=50)
    rubro = models.ForeignKey(Rubro, verbose_name=("Rubro"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['-id']

    def __str__(self):
        return self.rut