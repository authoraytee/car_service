from django.urls import path
 
from .views import ( # Запчасти авто
    AutopartsView,
)


urlpatterns = [
    # Домашняя страница каталога шиномонтажа
    path('', AutopartsView, name='auto_parts'),

]