# Generated by Django 2.2.5 on 2020-03-07 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FastMotorsApp', '0008_auto_20200307_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supervisorentry',
            name='total_amount',
            field=models.IntegerField(),
        ),
    ]