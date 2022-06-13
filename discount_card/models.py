from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

 
class DiscountCard(models.Model):
    card_number = models.CharField(max_length=8, default=None, verbose_name='Номер карты')

    card_owner = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
