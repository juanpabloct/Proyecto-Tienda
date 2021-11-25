from django import forms
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from Productos.models import Productos, Category
from clientes.forms import ProductoForm, TecnologiaForm, ProductoForm, accesorios_hogarForm, genero, form_category
# Create your views here.E


def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def delete(request, id):
    producto_a_borrar = Productos.objects.get(id=id)
    producto_a_borrar.delete()
    return redirect('Inicio')


def crearCategoria(request):
    if request.method == 'POST':
        form = form_category(request.method)
        code = request.POST.get('code')
        name = request.POST.get('name')
        guaardar = Category.objects.create(code=code, name=name)
        return redirect('Inicio')
    else:
        form = form_category
        return render(request, 'crearCategoria.html', {'form': form})


def categoria(request, category):
    all_products = Productos.objects.all()
    productos = Productos.objects.filter(categories__code=category)
    return render(request, 'categoria.html', {'all_products': productos, 'category': category})


def compras(request):
    return render(request, 'compras.html')


def actualizar(request, id):
    producto = Productos.objects.get(id=id)
    if request.method == 'POST':
        form = ProductoForm(request.method)
        fields = form.fields
        marca = request.POST.get('marca')
        referencia = request.POST.get('referencia')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        estado = request.POST.get('estado')

        producto.marca = marca
        producto.referencia = referencia
        producto.descripcion = descripcion
        producto.precio = precio
        producto.estado = estado
        producto.save()
        return redirect('Inicio')
    form = ProductoForm(initial = producto.__dict__)
    dato = {
        'form': form,
        'id': id
    }
    return render(request, 'actualizar.html', dato)


def tecnologia(request, tipo):
    tecnology_form = TecnologiaForm
    return render(request, 'tecnologia.html', {'forms': tecnology_form})


def genero_form(request, tipo):
    ropa_form = genero
    if request.method == 'POST':
        return redirect('ropa', tipo)
    else:
        return render(request, 'genero.html', {'forms': ropa_form, 'tipo': tipo})


def crear(request, category):
    form = ProductoForm
    return render(
        request, 'crear_producto.html', {'form': form, 'category': category}
    )


def guardar(request, category):
    if request.method == 'POST':
        form = ProductoForm(request.method)
        articulo = request.POST.get('articulo')
        marca = request.POST.get('marca')
        referencia = request.POST.get('referencia')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        estado = request.POST.get('estado')

        producto = Productos.objects.create(
            marca=marca,
            referencia=referencia,
            descripcion=descripcion,
            precio=precio,
            estado=estado,
        )
        producto.categories.add(Category.objects.get(code=category))
        producto.save()
    return redirect('categoria', category)
