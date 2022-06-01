from django.db import models
from django.db.models import Model

class Contacts(Model):
    city = models.CharField(max_length=100, default="г.Красноярск")
    street = models.CharField(max_length=100, default="ул. Красноярская")
    building = models.CharField(max_length=100, default="22")
    phone_number = models.CharField(max_length=10, default="9999999999")
    email = models.EmailField()
    postcode = models.CharField(max_length=6, default="660125")

    opening_hours = models.TimeField(auto_now=False, auto_now_add=False, default='09:00')
    closing_hours = models.TimeField(auto_now=False, auto_now_add=False, default='20:00')

    def __str__(self):
        return self.city + self.street + self.building