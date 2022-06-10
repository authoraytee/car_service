from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Car



CAR_FIELDS = [
            'brand',
            'model', 
            'engine', 
            'transmission',
            'steering_wheel', 
            'wheel_drive_type', 
        ]

#  Обработка машины ------------------------------------------------------
class CarCreate(CreateView):
    model = Car
    fields = CAR_FIELDS
    template_name = 'accounts/user_car/create_car.html'
    success_url = reverse_lazy('user_profile')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

class CarUpdate(UpdateView):
    model = Car
    fields = CAR_FIELDS
    template_name = 'accounts/user_car/update_car.html'
    success_url = reverse_lazy('user_profile')

class CarDelete(DeleteView): 
    model = Car
    template_name = 'accounts/user_car/delete_car.html'
    success_url = reverse_lazy('user_profile')
