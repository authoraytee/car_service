from django.urls import path
 
from .views import ( # Шиномонтаж
    TireFittingCatalogView,
    ChangeTireCatalogView,
    FixTireCatalogView,
    AllCarsCatalogView,
)


urlpatterns = [
    # Домашняя страница каталога шиномонтажа
    path('', TireFittingCatalogView, name='tire_fitting_catalog'),

    path('all_cars/', AllCarsCatalogView, name='all_cars'),
    path('change_tire/', ChangeTireCatalogView, name='change_tire'),
    path('fix_tire/', FixTireCatalogView, name='fix_tire'),
]