from django.contrib import admin
from .models import Contacts
from django.contrib.admin import ModelAdmin

@admin.register(Contacts)
class ContactsAdmin(ModelAdmin):
    pass