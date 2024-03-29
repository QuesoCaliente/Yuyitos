# Generated by Django 3.1.2 on 2020-11-11 04:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0008_auto_20201111_0111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='familia',
        ),
        migrations.AddField(
            model_name='producto',
            name='familia',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='producto.familia', verbose_name='Familia'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_vencimiento',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha Vencimiento'),
        ),
    ]
