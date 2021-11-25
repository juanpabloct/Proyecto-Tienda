from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from Productos.models import Productos
import json
from clientes.forms import accesorios_hogarForm, ProductoForm, TecnologiaForm, genero
from django.http import HttpResponse
# Create your views here.


def productos(request):
    all_products = Productos.objects.all()
    print(all_products)
    return render(request, 'productos.html', {"products": all_products, })


dict_productos = {
    'Tecnologia': ['Computadores', 'Celulares', 'Tablets', 'Consolas'],
    'Ropa': {
        'hombres': ['Camisas', 'Pantalones', 'Zapatos', 'Accesorios'],
        'mujeres': ['Camisas', 'Pantalones', 'Zapatos', 'Accesorios', 'Bolsos', 'Aretes']
    },
    'Accesorios para el hogar': ['Cocina', 'Electrodomesticos', 'Jardin', 'Muebles', 'Herramientas'],
}
def lista(request):
    if request.method == 'POST':
        post_data = json.loads(request.body.decode("utf-8"))
        name = post_data['tipo']
        print(request.POST)
        if name in dict_productos:
            return JsonResponse({'lista': dict_productos[name]})
        else:
            return JsonResponse({'lista': []})


def crud(request):
    productos_form = ProductoForm
    if request.method=='POST':
        valor=request.POST.get('tipo')
        if valor == 'Tecnologia':
            productos_form=TecnologiaForm
            return render(request, 'crud.html', {'tipo':productos_form})
        elif valor == 'Ropa':
            productos_form=genero()
            if request.method=='POST':
                Genero=request.POST.get('genero')
                print(Genero)
            return render(request, 'crud.html', {'genero':productos_form})
    return render(request, 'crud.html', {"tipo": productos_form})