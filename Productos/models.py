from django.db import models
from django.db.models.base import Model
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=15, null=True)
    def __str__(self):
        return self.name

class Productos(models.Model):
    marca=models.CharField(max_length=28, null=True)
    referencia=models.CharField(max_length=28, null=True)
    descripcion=models.TextField(null=True)
    precio=models.IntegerField(null=True)
    estado=models.CharField( max_length=10, null=True)
    categories = models.ManyToManyField(Category)

