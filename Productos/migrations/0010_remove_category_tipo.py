# Generated by Django 3.2.8 on 2021-11-22 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0009_category_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='tipo',
        ),
    ]
