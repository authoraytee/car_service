from django.urls import path
 
from .views import (
    HomeView,
    ContactsView,
    AboutView,
    DiscountsView
)


urlpatterns = [
    path('', HomeView, name='home'),
    path('contacts/', ContactsView, name='contacts'),
    path('about/', AboutView, name='about'),
    path('discounts', DiscountsView, name='discounts'),
]