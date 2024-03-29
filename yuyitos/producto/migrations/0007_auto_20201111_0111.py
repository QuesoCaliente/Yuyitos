# Generated by Django 3.1.2 on 2020-11-11 04:11

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0001_initial'),
        ('producto', '0006_auto_20201111_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_vencimiento',
            field=models.DateField(default=datetime.datetime(2020, 11, 11, 4, 11, 13, 422387, tzinfo=utc), verbose_name='Fecha Vencimiento'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedor.proveedor', verbose_name='Proveedor'),
        ),
    ]
