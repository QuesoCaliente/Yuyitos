from django.shortcuts import render, redirect
from .models import Producto
from .forms import productoForm
from django.utils import timezone

# Create your views here.
def ProductoView(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        return render(request, 'productos/lista_productos.html', {'productos': productos})

def ProductoCreateView(request):
    if request.method == 'POST':
        form = productoForm(request.POST)
        if form.is_valid():
            fechaVenc = form.cleaned_data['fecha_vencimiento']
            fechaVenc = str(fechaVenc)
            prov = form.cleaned_data['proveedor']
            fam = form.cleaned_data['familia']
            
            
            nuevo_registro = form.save()
            nuevo_registro.codigo_producto = getProductCode(prov.id, fam.id, fechaVenc, nuevo_registro.id )
            nuevo_registro.save()
            return redirect('listarProductos')
    else:
        form = productoForm()
    return render(request, 'productos/crear.html', {'form': form})


def ProductoEditView(request, producto_id):
    producto = Producto.objects.get(id = producto_id)
    if request.method == 'GET':
        form = productoForm(instance=producto)
    else:
        form = productoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listarProductos')
    return render(request, 'productos/crear.html', {'form': form} )


def ProductoDeleteView(request, producto_id):
    producto = Producto.objects.get(id = producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listarProductos')
    return render(request, 'productos/eliminar.html', {'producto': producto})
        

def getProductCode(proveedor, familia, fechaV, producto):
    codproducto = ''
    if proveedor <=9:
        codproducto +=f'00{proveedor}'
    elif proveedor >=10 and proveedor >=99:
        codproducto +=f'0{proveedor}'
    elif proveedor >=100:
        codproducto +=f'{proveedor}'  
        #Fin Proveedor

    if familia<=9:
        codproducto +=f'00{familia}'
    elif familia >=10 and familia >=99:
        codproducto +=f'0{familia}'
    elif familia >=100:
        codproducto +=f'{familia}'  
        #Fin Producto
    year, month, day = (int(i) for i in fechaV.split('-'))
    if fechaV == timezone.now:
        codproducto+='00000000'
    elif day <=9 and month <=9:
        codproducto+=f'{year}0{month}0{day}'
    elif day <=9:
        codproducto+=f'{year}{month}0{day}'
    elif month <=9:
        codproducto+=f'{year}0{month}{day}'

    if producto<=9:
        codproducto +=f'00{producto}'
    elif producto >=10 and producto <=99:
        codproducto +=f'0{producto}'
    elif producto >=100:
        codproducto +=f'{producto}'  
        #Fin Producto
    return codproducto

    
    