from django.urls import path
from clientes.views import index
from clientes.views import compras, delete, actualizar, tecnologia, crear, categoria, genero_form, guardar, crearCategoria
urlpatterns = [
    path('categoria/<str:category>', categoria, name='categoria'),
    path('compras', compras, name='compras'),
    path('delete/<int:id>', delete, name='borrar'),
    path('actualizar/<int:id>', actualizar, name='actualizar'),
    path('tecnology_form/<str:category>', tecnologia, name='tecnology_form'),
    path('gender_clothes/<str:category>', genero_form, name='clothes_form'),
    path('crear/<str:category>', crear, name='crear'),
    path('Crear_categoria/', crearCategoria, name='crea_categoria'),
    path('guardar/<str:category>', guardar, name='guardar'),
    path('', index, name='Inicio'),
]
