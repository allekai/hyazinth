from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

# Sign Up and Registration Stuff
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class LogoutUserView(TemplateView):    
    def get(self, request):
        logout(request)
        messages.success(request, "Erfolgreich abgemeldet!")
        return redirect("home")  