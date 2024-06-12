from django.urls import path
from .views import (
    FahrtErstellenView,
    FahrtBearbeitenView,
    FahrtListView,
    FahrtLoeschenView,
)

urlpatterns = [
    path("erstellen/", FahrtErstellenView.as_view(), name="fahrt_erstellen"),
    path(
        "<int:pk>/bearbeiten/",
        FahrtBearbeitenView.as_view(),
        name="fahrt_bearbeiten",
    ),
    path("<int:pk>/loeschen/", FahrtLoeschenView.as_view(), name="fahrt_loeschen"),
    path("", FahrtListView.as_view(), name="fahrt_liste"),  # URL für die Fahrtenliste
]
