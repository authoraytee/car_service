from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import DiscountCard


@admin.register(DiscountCard)
class DiscountCardAdmin(ModelAdmin):
    pass


