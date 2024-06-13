from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Anmeldung, Pfadfinderfahrt
from .forms import (
    AnmeldungForm,
    PfadfinderfahrtForm,
)


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


class FahrtDetailView(DetailView):
    model = Pfadfinderfahrt
    template_name = "fahrten/fahrt_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["angemeldet"] = Anmeldung.objects.filter(
            user=self.request.user, fahrt=self.object
        ).exists()
        return context


class AnmeldungErstellenView(LoginRequiredMixin, CreateView):
    model = Anmeldung
    form_class = AnmeldungForm
    template_name = "fahrten/anmeldung_form.html"
    success_url = reverse_lazy("fahrt_liste")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AnmeldungBearbeitenView(LoginRequiredMixin, UpdateView):
    model = Anmeldung
    form_class = AnmeldungForm
    template_name = "fahrten/anmeldung_form.html"
    success_url = reverse_lazy("fahrt_liste")


class AnmeldungLoeschenView(LoginRequiredMixin, DeleteView):
    model = Anmeldung
    template_name = "fahrten/anmeldung_confirm_delete.html"
    success_url = reverse_lazy("fahrt_liste")


class AnmeldungListView(LoginRequiredMixin, ListView):
    model = Anmeldung
    template_name = "fahrten/anmeldung_list.html"
    context_object_name = "object_list"

    def get_queryset(self):
        now = timezone.now()
        return Anmeldung.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["aktuelle_anmeldungen"] = context["object_list"].filter(
            fahrt__end_zeit__gt=timezone.now()
        )
        context["vergangene_anmeldungen"] = context["object_list"].filter(
            fahrt__end_zeit__lte=timezone.now()
        )
        return context
