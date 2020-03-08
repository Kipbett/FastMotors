# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import F
from django.shortcuts import render
from  django.core.mail import send_mail
from .forms import SecurityEntryForm, SupervisorEntryForm
from .models import SupervisorEntry, SecurityEntry

# Create your views here.

# Index page
def index(request):

    return render(request, 'FastMotorsApp/index.html')

# Security Page
def security(request):
    security_form = SecurityEntryForm()
    if request.method == "POST":
        security_form= SecurityEntryForm(data=request.POST)
        #validate data enterd
        if security_form.is_valid():
            # Save data to the database if valid
            security_form.save(commit=True)
            # Send an email alert to the supervisor
            subject = "New Truck For Inspection"
            message = "The details are: \n" + security_form.cleaned_data['driver_name'] +' \n' + str(security_form.cleaned_data['truck_model']) + '\n' + security_form.cleaned_data['truck_registration']
            sender = 'security@fastmotors.co.ke'
            recipient = ['supervisor@fastmotors.co.ke']
            send_mail(subject, message, sender, recipient)
            return index(request)
    return render(request, "FastMotorsApp/security.html", {'security_form':security_form})

# Supervisor page
def supervisor(request):
    supervisor_form = SupervisorEntryForm()

    if request.method == 'POST':
        supervisor_form = SupervisorEntryForm(data=request.POST)
        # Checks if data entered is valid
        if supervisor_form.is_valid():
            # Saves data to the database.
            supervisor_form.save(commit=True)
            # Send Email to the owner
            subject = "Truck Inspection and The Estimated Price For Service"
            message = "Your truck {} has been recieved ant the estimated service price will be {}".format(supervisor_form.cleaned_data['truck_registration'], str(supervisor_form.cleaned_data['total_amount']))
            sender = 'supervisor@fastmotors.co.ke'
            recipient = [str(SecurityEntry.objects.filter(owner_email= F('owner_email')))]
            send_mail(subject, message, sender, recipient)
            return index(request)
    return render(request, 'FastMotorsApp/supervisor.html', {'supervisor_form':supervisor_form})
