from django import forms
from .models import Producto

class productoForm(forms.ModelForm):
    class Meta:
        model = Producto

        fields = [
            'nombre',
            'descripcion',
            'familia',
            'fecha_vencimiento',
            'precioCompra',
            'precioVenta',
            'marca',
            'stock',
            'codigo_producto',
            'proveedor',
        ]

        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'familia': 'Familia',
            'fecha_vencimiento': 'Fecha Vencimiento',
            'precioCompra': 'Precio Compra',
            'precioVenta': 'Precio Venta',
            'marca': 'Marca',
            'stock': 'Stock',
            'codigo_producto': 'Codigo Producto',
            'proveedor':'Proveedor',
        }

        widgets = {
            'nombre': forms.TextInput(),
            'descripcion': forms.TextInput(),
            'familia': forms.Select(),
            'fecha_vencimiento': forms.DateInput(),
            'precioCompra': forms.NumberInput(),
            'precioVenta': forms.NumberInput(),
            'marca': forms.Select(),
            'stock': forms.NumberInput(),
            'codigo_producto': forms.HiddenInput(),
            'proveedor': forms.Select(),
        }