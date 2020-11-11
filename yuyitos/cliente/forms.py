from django import forms
from .models import Cliente


class clienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

        fields = [
            'rut',
            'nombre',
            'apellidos',
            'direccion',
            'telefono',
            'correo',
        ]

        labels = {
            'rut': 'Rut',
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
            'correo': 'Correo'
        }

        widgets = {
            'rut': forms.TextInput(),
            'nombre': forms.TextInput(),
            'apellidos': forms.TextInput(),
            'direccion': forms.TextInput(),
            'telefono': forms.NumberInput(),
            'correo': forms.EmailInput(),
        }