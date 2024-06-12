from django.urls import path
from .views import (
    AnmeldungBearbeitenView,
    AnmeldungErstellenView,
    AnmeldungListView,
    AnmeldungLoeschenView,
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
    path(
        "anmeldung/erstellen/",
        AnmeldungErstellenView.as_view(),
        name="anmeldung_erstellen",
    ),
    path(
        "anmeldung/<int:pk>/bearbeiten/",
        AnmeldungBearbeitenView.as_view(),
        name="anmeldung_bearbeiten",
    ),
    path(
        "anmeldung/<int:pk>/loeschen/",
        AnmeldungLoeschenView.as_view(),
        name="anmeldung_loeschen",
    ),
    path("meine-anmeldungen/", AnmeldungListView.as_view(), name="meine_anmeldungen"),
]
