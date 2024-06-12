from django import forms
from .models import Pfadfinderfahrt


class PfadfinderfahrtForm(forms.ModelForm):
    class Meta:
        model = Pfadfinderfahrt
        fields = [
            "titel",
            "ziel",
            "beschreibung",
            "motto",
            "start_zeit",
            "end_zeit",
            "start_ort",
            "end_ort",
        ]
        widgets = {
            "start_zeit": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "end_zeit": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
