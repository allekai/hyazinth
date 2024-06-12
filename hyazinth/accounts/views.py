from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Sign Up and accounts Stuff
# See also https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication#project_urls
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("profile")
    template_name = "registration/signup.html"


class LogoutUserView(TemplateView):    
    def get(self, request):
        logout(request)
        messages.success(request, "Erfolgreich abgemeldet!")
        return redirect("home")  


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "registration/profile.html"
    
    def get(self, request):
        messages.success(request, f"Hello {request.user.username}")
        return render(request=request, template_name=self.template_name, context={"user": request.user})