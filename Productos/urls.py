from django.urls import path
from Productos.views import productos, crud, lista

urlpatterns = [
    path('crud/', crud, name='crud'),
    path('lista', lista, name='lista'),
    path('productos', productos, name='productos'),
]
