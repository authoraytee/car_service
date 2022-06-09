from django.urls import path
 
from .views import ( # Шиномонтаж
    TireFittingCatalogView,
    ChangeTireCatalogView,
    FixTireCatalogView,
    LightweightCarsCatalogView,
    MinubusesCatalogView,
    SuvCatalogView,
)


urlpatterns = [
    # Домашняя страница каталога шиномонтажа
    path('', TireFittingCatalogView, name='tire_fitting_catalog'),

    path('change_tire/', ChangeTireCatalogView, name='change_tire'),
    path('fix_tire/', FixTireCatalogView, name='fix_tire'),
    path('lightweight_cars/', LightweightCarsCatalogView, name='lightweight_cars'),
    path('minibuses/', MinubusesCatalogView, name='minibuses'),
    path('suv/', SuvCatalogView, name='suv'),
]