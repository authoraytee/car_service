from django.urls import path
 
from .views import (
    HomeView,
    ContactsView,
    DiscountsView
)


urlpatterns = [
    path('', HomeView, name='home'),
    path('contacts/', ContactsView, name='contacts'),
    path('discounts', DiscountsView, name='discounts'),
]