from django.urls import path
 

from .views import ( # Обработка кнопки
    ExternalWashingView,

)

urlpatterns = [

    # Внешняя мойка -------------------
    path('external_washing/', ExternalWashingView.as_view(), name='external_washing'),
]