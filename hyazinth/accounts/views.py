from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


# Sign Up and accounts Stuff
# See also https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication#project_urls
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
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
        messages.success(request, f"Hello {request.user.first_name}")
        return render(
            request=request,
            template_name=self.template_name,
            context={"user": request.user},
        )


class ProfileUpdateView(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("profile")  # Oder eine andere Erfolgsseite
    template_name = "accounts/profile_update.html"

    def get_object(self):
        return self.request.user


# Admin Viewws
@method_decorator(staff_member_required, name="get")
class UserListView(ListView):
    model = User
    paginate_by = 100
    template_name = "accounts/user_list.html"
    context_object_name = "users"
