# Generated by Django 3.1.2 on 2020-11-11 04:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0007_auto_20201111_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_vencimiento',
            field=models.DateField(default=datetime.datetime(2020, 11, 11, 4, 11, 46, 68013, tzinfo=utc), verbose_name='Fecha Vencimiento'),
        ),
    ]
