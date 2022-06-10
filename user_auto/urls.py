from django.urls import path
 
from .views import ( # Машина
    CarCreate,
    CarUpdate,
    CarDelete,
)


urlpatterns = [
    # Машины пользователя -------------------
    path('create_car', CarCreate.as_view(), name='car_create'),
    path('update_car/<int:pk>', CarUpdate.as_view(), name='car_update'),
    path('delete_car/<int:pk>', CarDelete.as_view(), name='car_delete'),
]