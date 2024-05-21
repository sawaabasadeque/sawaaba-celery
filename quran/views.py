# quran/views.py

from django.shortcuts import render
from .models import Surah, Ayah

def index(request):
    surahs = Surah.objects.prefetch_related('ayahs').order_by('number')
    # Now each Surah's Ayahs are sorted within the template loop
    return render(request, 'quran/index.html', {'surahs': surahs})
    

