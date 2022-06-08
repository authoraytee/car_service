from django.urls import path
 
from .views import ( # Шиномонтаж
    TireFittingCatalogView,
    # ExternalWashingCreate,
    # ExternalWashingUpdate,
    # ExternalWashingDelete,
)


urlpatterns = [
    # Домашняя страница каталога шиномонтажа
    path('', TireFittingCatalogView, name='tire_fitting_catalog'),


    # # Внешняя мойка -------------------
    # path('external_washing/', ExternalWashingView.as_view(), name='external_washing'),
    # path('external_washing/create', ExternalWashingCreate.as_view(), name='external_washing_create'),
    # path('external_washing/update/<int:pk>', ExternalWashingUpdate.as_view(), name='external_washing_update'),
    # path('external_washing/delete/<int:pk>', ExternalWashingDelete.as_view(), name='external_washing_delete'),

]