# quran/models.py

from django.db import models

class Surah(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    arabic_name = models.CharField(max_length=100)
    total_verses = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.arabic_name})"

class Ayah(models.Model):
    surah = models.ForeignKey(Surah, on_delete=models.CASCADE, related_name='ayahs')
    number_in_surah = models.IntegerField()
    arabic_text = models.TextField()
    juz = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('surah', 'number_in_surah')

    def __str__(self):
        return f"{self.surah.name} Ayah {self.number_in_surah}"
