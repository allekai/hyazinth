from django.db import models
from django.utils import timezone

from accounts.models import User


class Pfadfinderfahrt(models.Model):
    titel = models.CharField(max_length=255)
    ziel = models.CharField(max_length=255, blank=True, null=True)  # Ziel optional
    start_zeit = models.DateTimeField(default=timezone.now)
    end_zeit = models.DateTimeField(default=timezone.now)
    start_ort = models.CharField(max_length=255)
    end_ort = models.CharField(max_length=255)
    beschreibung = models.TextField(blank=True)
    motto = models.CharField(max_length=255, blank=True, null=True)  # Motto optional

    def __str__(self):
        return f"Pfadfinderfahrt: {self.titel} ({self.start_zeit.strftime('%Y-%m-%d')})"


class Anmeldung(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fahrt = models.ForeignKey(Pfadfinderfahrt, on_delete=models.CASCADE)
    anmelde_zeitpunkt = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "fahrt")  # Jede Fahrt pro Benutzer nur einmal
