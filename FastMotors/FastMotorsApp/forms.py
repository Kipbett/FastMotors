from django import forms
from .models import SecurityEntry, SupervisorEntry, TruckParts
from django.db.models import F


class SecurityEntryForm(forms.ModelForm):
    class Meta:
        model = SecurityEntry
        fields = '__all__'

class SupervisorEntryForm(forms.ModelForm):
    model_price = TruckParts.objects.filter(service_price=F('service_price'))
    service_type = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=TruckParts.objects.filter(model= F("model")))
    class Meta:
        model = SupervisorEntry
        fields = ('truck_registration', 'truck_model', 'service_type', 'service_parts', 'total_amount')