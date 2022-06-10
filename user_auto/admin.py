from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Car


@admin.register(Car)
class CarAdmin(ModelAdmin):
    pass

