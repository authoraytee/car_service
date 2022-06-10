from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

from django.views.generic import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin

from user_auto.models import Car

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserProfile(ListView):
    model = get_user_model()
    template_name = "accounts/user_profile.html"

    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        context['user_cars'] = Car.objects.all()

        context['current_user'] = self.request.user
        return context
