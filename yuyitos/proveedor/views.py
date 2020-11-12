from django.shortcuts import render, redirect
from .forms import proveedorForm
from .models import Proveedor
# Create your views here.

def ProveedorView(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            proveedores = Proveedor.objects.all()
            return render(request, 'proveedores/lista_proveedores.html', {'proveedores': proveedores})
    else:
        return render(request, 'base/404.html', {})

def ProveedorCreateView(request):
    if request.method == 'POST':
        form = proveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarProveedores')
    else:
        form = proveedorForm()
    return render(request, 'proveedores/crear.html', {'form': form})

def ProveedorEditView(request, proveedor_id):
    proveedor = Proveedor.objects.get(id = proveedor_id)
    if request.method == 'GET':
        form = proveedorForm(instance=proveedor)
    else:
        form = proveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('listarProveedores')
    return render(request, 'proveedores/crear.html', {'form': form} )

def ProveedorDeleteView(request, proveedor_id):
    proveedor = Proveedor.objects.get(id = proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('listarProveedores')
    return render(request, 'proveedores/eliminar.html', {'proveedor': proveedor})
    