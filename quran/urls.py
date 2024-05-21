# quran/urls.py

from django.urls import path
from . import views

app_name = "quran"

urlpatterns = [
    path('', views.index, name='index'),
]
