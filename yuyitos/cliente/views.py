from django.shortcuts import render, redirect
from .forms import clienteForm
from .models import Cliente


def ClienteView(request):
    if request.method == 'GET':
        clientes = Cliente.objects.all()
        return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def ClienteCreateView(request):
    if request.method == 'POST':
        form = clienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarClientes')
    
    else:
        form = clienteForm()

    return render(request, 'clientes/crear.html', {'form':form})

def ClienteEditView(request, cliente_id):
    cliente = Cliente.objects.get(id = cliente_id)
    if request.method == 'GET':
        form = clienteForm(instance=cliente)
    else:
        form = clienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listarClientes')
    
    return render(request, 'clientes/crear.html', {'form': form})


def ClienteDeleteView(request, cliente_id):
    cliente = Cliente.objects.get(id= cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listarClientes')
    return render(request, 'clientes/eliminar.html', {'cliente': cliente})