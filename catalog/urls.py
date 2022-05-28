from django.urls import path
 
from .views import (
    HomeView,
    ContactsView,
)

urlpatterns = [
    path('', HomeView, name='home'),


    path('contacts', ContactsView, name='contacts'),
]