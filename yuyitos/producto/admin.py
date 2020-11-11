from django.contrib import admin
from .models import Producto, Familia, Marca
# Register your models here.

admin.site.register(Producto)
admin.site.register(Familia)
admin.site.register(Marca)