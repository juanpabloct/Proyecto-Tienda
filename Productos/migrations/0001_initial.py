# Generated by Django 3.2.8 on 2021-11-03 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=28)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
    ]