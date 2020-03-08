# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import TruckModels, TruckParts, SecurityEntry, SupervisorEntry

# Register your models here.

class TruckPartsAdmin(admin.ModelAdmin):

    search_fields = ['description']
    list_display = ['part_no', 'description', 'service_price', 'model']

class SecurityEntryAdmin(admin.ModelAdmin):
    search_fields = ['truck_registration']
    list_display = ['driver_name', 'company_name', 'owner_name', 'truck_model', 'truck_registration']

admin.site.register(TruckParts, TruckPartsAdmin)
admin.site.register(TruckModels)
admin.site.register(SecurityEntry, SecurityEntryAdmin)
admin.site.register(SupervisorEntry)
