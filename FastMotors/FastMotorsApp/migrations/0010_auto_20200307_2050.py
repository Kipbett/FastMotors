# Generated by Django 2.2.5 on 2020-03-07 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FastMotorsApp', '0009_auto_20200307_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supervisorentry',
            name='service_parts',
            field=models.TextField(max_length=1000),
        ),
    ]
