from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import (
    ExternalWashing,
    InternalWashing,
    Polishing,
    DryCleaning,
)

ALL_MODELS_FIELDS = [
            'washing_object',
            'light_weight_car_price', 
            'universal_car_price', 
            'minivan_car_price',
            'suv_car_price', 
            'minibus_car_price', 
        ]


def CarWashCatalogView(request):
    return render(request,'car_wash/car_wash_catalog.html')


#  Внешняя мойка ------------------------------------------------------
class ExternalWashingView(ListView):
    model = ExternalWashing
    template_name = "car_wash/external_washing/external_washing.html"

class ExternalWashingCreate(CreateView):
    model = ExternalWashing
    fields = ALL_MODELS_FIELDS
    template_name = 'car_wash/external_washing/create_external_washing.html'
    success_url = reverse_lazy('external_washing')

class ExternalWashingUpdate(UpdateView):
    model = ExternalWashing
    fields = ALL_MODELS_FIELDS
    template_name = 'car_wash/external_washing/update_external_washing.html'
    success_url = reverse_lazy('external_washing')

class ExternalWashingDelete(DeleteView): 
    model = ExternalWashing
    fields = ALL_MODELS_FIELDS
    template_name = 'car_wash/external_washing/delete_external_washing.html'
    success_url = reverse_lazy('external_washing')


# Внутренняя мойка ----------------------------------------------------
class InternalWashingView(ListView):
    model = InternalWashing
    template_name = "car_wash/internal_washing/internal_washing.html"

class InternalWashingCreate(CreateView):
    model = InternalWashing
    fields = ALL_MODELS_FIELDS
    template_name = 'car_wash/internal_washing/create_internal_washing.html'
    success_url = reverse_lazy('internal_washing')

class InternalWashingUpdate(UpdateView):
    model = InternalWashing
    fields = ALL_MODELS_FIELDS
    template_name = 'car_wash/internal_washing/update_internal_washing.html'
    success_url = reverse_lazy('internal_washing')

class InternalWashingDelete(DeleteView): 
    model = InternalWashing
    fields = ALL_MODELS_FIELDS
    template_name = 'car_wash/internal_washing/delete_internal_washing.html'
    success_url = reverse_lazy('internal_washing')


# Полировка -----------------------------------------------------------
class PolishingView(ListView):
    model = Polishing
    template_name = "car_wash/polishing/polishing.html"

class PolishingCreate(CreateView):
    model = Polishing
    fields = ALL_MODELS_FIELDS
    template_name = 'car_wash/polishing/create_polishing.html'
    success_url = reverse_lazy('polishing')

class PolishingUpdate(UpdateView):
    model = Polishing
    fields = ALL_MODELS_FIELDS
    template_name = 'car_wash/polishing/update_polishing.html'
    success_url = reverse_lazy('polishing')

class PolishingDelete(DeleteView): 
    model = Polishing
    fields = ALL_MODELS_FIELDS
    template_name = 'car_wash/polishing/delete_polishing.html'
    success_url = reverse_lazy('polishing')


# Химчистка -----------------------------------------------------------
class DryCleaningView(ListView):
    model = DryCleaning
    template_name = "car_wash/dry_cleaning/dry_cleaning.html"

class DryCleaningCreate(CreateView):
    model = DryCleaning
    fields = ALL_MODELS_FIELDS
    template_name = 'car_wash/dry_cleaning/create_dry_cleaning.html'
    success_url = reverse_lazy('dry_cleaning')

class DryCleaningUpdate(UpdateView):
    model = DryCleaning
    fields = ALL_MODELS_FIELDS
    template_name = 'car_wash/dry_cleaning/update_dry_cleaning.html'
    success_url = reverse_lazy('dry_cleaning')

class DryCleaningDelete(DeleteView): 
    model = DryCleaning
    fields = ALL_MODELS_FIELDS
    template_name = 'car_wash/dry_cleaning/delete_dry_cleaning.html'
    success_url = reverse_lazy('dry_cleaning')