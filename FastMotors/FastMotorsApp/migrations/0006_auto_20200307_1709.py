# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-07 17:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FastMotorsApp', '0005_supervisorentry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supervisorentry',
            name='service_price',
        ),
        migrations.AlterField(
            model_name='supervisorentry',
            name='service_parts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FastMotorsApp.TruckParts'),
        ),
    ]
