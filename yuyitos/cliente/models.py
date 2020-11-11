from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key = True)
    rut = models.CharField('Rut', max_length=12)
    nombre = models.CharField('Nombre', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=100)
    direccion = models.CharField('Direccion', max_length=50)
    telefono = models.IntegerField('Telefono')
    correo = models.EmailField('Correo', max_length=254)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.rut