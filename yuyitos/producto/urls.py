from django.urls import path, include
from .views import ProductoView, ProductoCreateView, ProductoEditView, ProductoDeleteView
urlpatterns = [
    path('', ProductoView, name='listarProductos' ),
    path('crear/', ProductoCreateView, name='crearProducto' ),
    path('editar/<int:producto_id>', ProductoEditView, name='editarProducto'),
    path('eliminar/<int:producto_id>', ProductoDeleteView, name='eliminarProducto')
]