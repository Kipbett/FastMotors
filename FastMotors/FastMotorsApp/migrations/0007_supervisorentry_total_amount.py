# Generated by Django 2.2.5 on 2020-03-07 20:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FastMotorsApp', '0006_auto_20200307_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='supervisorentry',
            name='total_amount',
            field=models.IntegerField(),
            preserve_default=False,
        ),
    ]