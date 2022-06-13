from discount_card.models import DiscountCard
from random import randint
from django.contrib.auth import get_user_model

User = get_user_model()

card_number = randint(10000000, 99999999)

print(card_number)