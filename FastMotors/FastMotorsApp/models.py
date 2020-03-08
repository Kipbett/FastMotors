# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Create car models in the admin
class TruckModels(models.Model):
    model_name = models.CharField(max_length=200)

    def __str__(self):
        return self.model_name

# Create models for car part for service and their prices
class TruckParts(models.Model):
    part_no = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    service_price = models.PositiveIntegerField()
    model = models.ForeignKey(TruckModels, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.description } ({self.model}) ({self.service_price})'

class SecurityEntry(models.Model):
    driver_name = models.CharField(max_length=100)
    driver_phone = models.IntegerField()
    company_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    owner_email = models.EmailField()
    truck_model = models.ForeignKey(TruckModels, on_delete=models.CASCADE)
    truck_registration = models.CharField(max_length=100)
    truck_chassis = models.IntegerField()
    engine_number = models.CharField(max_length=50)
    car_mileage = models.IntegerField()

    def __str__(self):
        return self.truck_registration

class SupervisorEntry(models.Model):
    truck_registration = models.ForeignKey(SecurityEntry, on_delete=models.CASCADE)
    truck_model = models.ForeignKey(TruckModels, on_delete=models.CASCADE)
    service_parts = models.TextField(max_length=1000)
    total_amount = models.IntegerField()
