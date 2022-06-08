from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

from django.views.generic import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserProfile(PermissionRequiredMixin, ListView):
    context_object_name = 'home_list'
    permission_required = 'app.view_event'    
    model = get_user_model()
    template_name = "accounts/user_profile.html"
