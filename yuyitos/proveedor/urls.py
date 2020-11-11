from django.urls import path, include
from proveedor.views import ProveedorView, ProveedorCreateView, ProveedorEditView, ProveedorDeleteView

urlpatterns = [
    path('', ProveedorView,  name='listarProveedores'),
    path('crear/', ProveedorCreateView,  name='crearProveedor'),
    path('editar/<int:proveedor_id>', ProveedorEditView,  name='editarProveedor'),
    path('eliminar/<int:proveedor_id>', ProveedorDeleteView,  name='eliminarProveedor'),
]