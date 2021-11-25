from django import forms
from django.forms.widgets import Select
class TecnologiaForm(forms.Form):
    producto=forms.ChoiceField(choices=(('Computadores','Computadores'), ('Celulares', 'Celulares'), ('Tablets', 'Tablets'), ('Consolas', 'Consolas'),))
    marca=forms.CharField(max_length=100)
    referencia=forms.CharField(max_length=100)
    descripcion=forms.TextInput()
    precio=forms.NumberInput()
    estado=forms.ChoiceField(choices=(('nuevo','nuevo'), ('usado', 'usado'),))
class genero(forms.Form):
    genero=forms.ChoiceField(choices=(('hombre','hombre'), ('mujer', 'mujer'),))
class ProductoForm(forms.Form):
    marca=forms.CharField(max_length=100)
    referencia=forms.CharField(max_length=100)
    descripcion=forms.CharField()
    precio=forms.IntegerField()
    estado=forms.ChoiceField(choices=(('nuevo','nuevo'), ('usado', 'usado'),))
class accesorios_hogarForm(forms.Form):
    accesorios=forms.ChoiceField(choices=(('Cocina','Cocina'), ('Electrodomesticos', 'Electrodomesticos'), ('Jardin', 'Jardin'), ('Muebles', 'Muebles'), ('Herramientas', 'Herramientas'),))    
    marca=forms.CharField(max_length=100)
    referencia=forms.CharField(max_length=100)
    descripcion=forms.Textarea()
    precio=forms.NumberInput()
    estado=forms.ChoiceField(choices=(('nuevo','nuevo'), ('usado', 'usado'),))
class form_category(forms.Form):
    name=forms.CharField(max_length=100)
    code=forms.CharField(max_length=10)