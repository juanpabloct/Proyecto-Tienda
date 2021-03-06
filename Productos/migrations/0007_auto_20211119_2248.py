# Generated by Django 3.2.9 on 2021-11-20 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0006_auto_20211118_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200, null=True)),
                ('code', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='productos',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='productos',
            name='tipo',
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
        migrations.DeleteModel(
            name='ropa',
        ),
        migrations.AddField(
            model_name='productos',
            name='categories',
            field=models.ManyToManyField(to='Productos.Category'),
        ),
    ]
