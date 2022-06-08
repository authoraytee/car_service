from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import ExternalWashing, InternalWashing, Polishing, DryCleaning


@admin.register(ExternalWashing)
class ExternalWashingAdmin(ModelAdmin):
    pass


@admin.register(InternalWashing)
class InternalWashingAdmin(ModelAdmin):
    pass


@admin.register(Polishing)
class PolishingAdmin(ModelAdmin):
    pass


@admin.register(DryCleaning)
class DryCleaningAdmin(ModelAdmin):
    pass

