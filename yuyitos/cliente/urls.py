from django.urls import path, include
from cliente.views import ClienteView, ClienteCreateView, ClienteEditView, ClienteDeleteView

urlpatterns = [
    path('', ClienteView,  name='listarClientes'),
    path('crear/', ClienteCreateView,  name='crearCliente'),
    path('editar/<int:cliente_id>', ClienteEditView,  name='editarCliente'),
    path('eliminar/<int:cliente_id>', ClienteDeleteView,  name='eliminarCliente'),
]