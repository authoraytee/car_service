from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# from .models import (
#     ExternalWashing,
#     InternalWashing,
#     Polishing,
#     DryCleaning,
# )

ALL_MODELS_FIELDS = [
            'washing_object',
            'light_weight_car_price', 
            'universal_car_price', 
            'minivan_car_price',
            'suv_car_price', 
            'minibus_car_price', 
        ]


def AutopartsCatalogView(request):
    return render(request,'auto_parts/auto_parts_catalog.html')
