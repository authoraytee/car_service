from django import forms

from .models import CustomUser

class ManagerLoginForm(forms.ModelForm):

    class Meta:
       model = CustomUser
       fields = ['email', 'password', ]