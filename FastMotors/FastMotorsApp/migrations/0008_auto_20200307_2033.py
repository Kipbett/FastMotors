# Generated by Django 2.2.5 on 2020-03-07 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FastMotorsApp', '0007_supervisorentry_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supervisorentry',
            name='total_amount',
            field=models.PositiveIntegerField(),
        ),
    ]
