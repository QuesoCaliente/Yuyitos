# Generated by Django 3.1.2 on 2020-10-26 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('codigo_familia', models.CharField(max_length=100, verbose_name='Codigo Familia')),
            ],
            options={
                'verbose_name': 'Familia',
                'verbose_name_plural': 'Familias',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.TextField(max_length=255, verbose_name='Descripcion')),
                ('precioCompra', models.IntegerField(verbose_name='Precio Compra')),
                ('precioVenta', models.IntegerField(verbose_name='Precio Venta')),
                ('stock', models.IntegerField()),
                ('familia', models.ManyToManyField(to='producto.Familia', verbose_name='Familia')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.marca', verbose_name='Marca')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
    ]