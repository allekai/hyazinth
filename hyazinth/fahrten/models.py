from django.db import models
from django.utils import timezone


class Pfadfinderfahrt(models.Model):
    titel = models.CharField(max_length=255)
    ziel = models.CharField(max_length=255)  # Ziel als String
    beschreibung = models.TextField(blank=True)
    motto = models.CharField(max_length=255)
    start_zeit = models.DateTimeField(default=timezone.now)
    end_zeit = models.DateTimeField(default=timezone.now)
    start_ort = models.CharField(max_length=255)  # Startort als String
    end_ort = models.CharField(max_length=255)  # Endort als String
