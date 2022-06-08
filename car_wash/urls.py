from django.urls import path
 
from .views import CarWashCatalogView

from .views import ( # Внешняя мойка
    ExternalWashingView,
    ExternalWashingCreate,
    ExternalWashingUpdate,
    ExternalWashingDelete,
)
from .views import ( # Внутренняя мойка
    InternalWashingView,
    InternalWashingCreate,
    InternalWashingUpdate,
    InternalWashingDelete,
)
from .views import ( # Полировка
    PolishingView,
    PolishingCreate,
    PolishingUpdate,
    PolishingDelete,
)
from .views import ( # Химчистка
    DryCleaningView,
    DryCleaningCreate,
    DryCleaningUpdate,
    DryCleaningDelete,
)


urlpatterns = [
    # Домашняя страница каталога мойки
    path('', CarWashCatalogView, name='car_wash_catalog'),


    # Внешняя мойка -------------------
    path('external_washing/', ExternalWashingView.as_view(), name='external_washing'),
    path('external_washing/create', ExternalWashingCreate.as_view(), name='external_washing_create'),
    path('external_washing/update/<int:pk>', ExternalWashingUpdate.as_view(), name='external_washing_update'),
    path('external_washing/delete/<int:pk>', ExternalWashingDelete.as_view(), name='external_washing_delete'),

    # Внутренняя мойка ----------------
    path('internal_washing/', InternalWashingView.as_view(), name='internal_washing'),
    path('internal_washing/create', InternalWashingCreate.as_view(), name='internal_washing_create'),
    path('internal_washing/update/<int:pk>', InternalWashingUpdate.as_view(), name='internal_washing_update'),
    path('internal_washing/delete/<int:pk>', InternalWashingDelete.as_view(), name='internal_washing_delete'),

    # Полировка -----------------------
    path('polishing/', PolishingView.as_view(), name='polishing'),
    path('polishing/create', PolishingCreate.as_view(), name='polishing_create'),
    path('polishing/update/<int:pk>', PolishingUpdate.as_view(), name='polishing_update'),
    path('polishing/delete/<int:pk>', PolishingDelete.as_view(), name='polishing_delete'),

    # Химчистка ----------------------
    path('dry_cleaning/', DryCleaningView.as_view(), name='dry_cleaning'),
    path('dry_cleaning/create', DryCleaningCreate.as_view(), name='dry_cleaning_create'),
    path('dry_cleaning/update/<int:pk>', DryCleaningUpdate.as_view(), name='dry_cleaning_update'),
    path('dry_cleaning/delete/<int:pk>', DryCleaningDelete.as_view(), name='dry_cleaning_delete'),
]