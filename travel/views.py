# travel/views.py

import os
from django.shortcuts import render

def index(request):
    return render(request, 'travel/index.html')

# Notification:
from .utils import send_push_notification

def my_view(request):
    # Your view logic here
    registration_id = "device_registration_id"  # Replace with the actual registration ID of the device
    send_push_notification(registration_id, "Notification Title", "Notification Body")
    return render(request, "travel/thank_you.html")
