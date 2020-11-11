from django import forms
from .models import Proveedor


class proveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor

        fields = [
            'rut',
            'nombre',
            'correo',
            'telefono',
            'direccion',
            'rubro',
        ]

        labels = {
            'rut': 'Rut',
            'nombre': 'Nombre',
            'correo': 'Correo',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'rubro': 'Rubro'
        }

        widgets = {
            'rut': forms.TextInput(),
            'nombre': forms.TextInput(),
            'correo': forms.EmailInput(),
            'telefono': forms.NumberInput(),
            'direccion': forms.TextInput(),
            'rubro': forms.Select()
        }