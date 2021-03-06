# Generated by Django 3.2.9 on 2021-11-19 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0005_alter_productos_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='ropa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ropa', models.CharField(max_length=28, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='productos',
            name='imagen',
        ),
        migrations.AlterField(
            model_name='productos',
            name='descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='precio',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='producto',
            field=models.CharField(max_length=28, null=True),
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Productos.ropa')),
            ],
        ),
    ]
