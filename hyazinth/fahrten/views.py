from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Pfadfinderfahrt
from .forms import PfadfinderfahrtForm  # Du musst ein Formular erstellen (siehe unten)


class FahrtErstellenView(CreateView):
    model = Pfadfinderfahrt
    form_class = PfadfinderfahrtForm
    template_name = "fahrten/fahrt_form.html"  # Erstelle diese Vorlage
    success_url = reverse_lazy("fahrt_liste")  # Erstelle diese URL/View


class FahrtBearbeitenView(UpdateView):
    model = Pfadfinderfahrt
    form_class = PfadfinderfahrtForm
    template_name = "fahrten/fahrt_form.html"
    success_url = reverse_lazy("fahrt_liste")


class FahrtLoeschenView(DeleteView):
    model = Pfadfinderfahrt
    template_name = "fahrten/fahrt_confirm_delete.html"  # Erstelle diese Vorlage
    success_url = reverse_lazy("fahrt_liste")


class FahrtListView(ListView):
    model = Pfadfinderfahrt
    template_name = "fahrten/fahrt_list.html"
    context_object_name = (
        "object_list"  # Optional, um den Kontextnamen in der Vorlage anzupassen
    )
